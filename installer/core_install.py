# -*- coding: utf-8 -*-
#
# (c) Copyright 2003-2007 Hewlett-Packard Development Company, L.P.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# Author: Don Welch
#

# Std Lib
import sys
import os
import os.path
import re
import time
import cStringIO
import grp
import pwd
import urllib # TODO: Replace with urllib2 (urllib is deprecated in Python 3.0)
import sha # TODO: Replace with hashlib (sha is deprecated in Python 3.0)
import tarfile

# Local
from base.g import *
from base.codes import *
from base import utils, pexpect
from dcheck import *

DISTRO_UNKNOWN = 0
DISTRO_VER_UNKNOWN = '0.0'

MODE_INSTALLER = 0 # hplip-install
MODE_CHECK = 1 # hp-check
MODE_CREATE_DOCS = 2 # create_docs

TYPE_STRING = 1
TYPE_LIST = 2
TYPE_BOOL = 3
TYPE_INT = 4

DEPENDENCY_RUN_TIME = 1
DEPENDENCY_COMPILE_TIME = 2
DEPENDENCY_RUN_AND_COMPILE_TIME = 3

PING_TARGET = "www.google.com"
HTTP_GET_TARGET = "http://www.google.com"

PASSWORD_LIST = [
    pexpect.EOF, # 0
    pexpect.TIMEOUT, # 1
    "passwor[dt]", # en/de/it/ru
    "kennwort", # de?
    "password for", # en
    "mot de passe", # fr
    "contraseña", # es
    "palavra passe", # pt
    "口令", # zh
    "wachtwoord", # nl
    "heslo", # czech
]

PASSWORD_EXPECT_LIST = []
for s in PASSWORD_LIST:
    try:
        p = re.compile(s, re.I)
    except TypeError:
        PASSWORD_EXPECT_LIST.append(s)
    else:
        PASSWORD_EXPECT_LIST.append(p)

OK_PROCESS_LIST = ['adpept-notifier', 
                   'yum-updatesd',
                   ]
                   
CONFIGURE_ERRORS = { 1 : "General/unknown error",
                     2 : "libusb not found",
                     3 : "cups-devel not found",
                     4 : "libnetsnmp not found",
                     5 : "netsnmp-devel not found",
                     6 : "python-devel not found",
                     7 : "pthread-devel not found",
                     8 : "ppdev-devel not found",
                     9 : "libcups not found",
                     10 : "libm not found",
                     11 : "libusb-devel not found",
                     12 : "sane-backends-devel not found",
                     13 : "libdbus not found",
                     14 : "dbus-devel not found",
                     15 : "fax requires dbus support",
                     102 : "libjpeg not found",
                     103 : "jpeg-devel not found",
                     104 : "libdi not found",
                   }


try:
    from functools import update_wrapper
except ImportError: # using Python version < 2.5
    def trace(f):
        def newf(*args, **kw):
           log.debug("TRACE: func=%s(), args=%s, kwargs=%s" % (f.__name__, args, kw))
           return f(*args, **kw)
        newf.__name__ = f.__name__
        newf.__dict__.update(f.__dict__)
        newf.__doc__ = f.__doc__
        newf.__module__ = f.__module__
        return newf
else: # using Python 2.5+
    def trace(f):
        def newf(*args, **kw):
            log.debug("TRACE: func=%s(), args=%s, kwargs=%s" % (f.__name__, args, kw))
            return f(*args, **kw)
        return update_wrapper(newf, f)



class CoreInstall(object):
    def __init__(self, mode=MODE_INSTALLER, ui_mode=INTERACTIVE_MODE):
        os.umask(0022)
        self.mode = mode
        self.ui_mode = ui_mode
        self.password = ''
        self.version_description, self.version_public, self.version_internal = '', '', ''
        self.bitness = 32
        self.endian = utils.LITTLE_ENDIAN
        self.distro, self.distro_name, self.distro_version = DISTRO_UNKNOWN, '', DISTRO_VER_UNKNOWN
        self.distro_version_supported = False
        self.install_location = '/usr'
        self.hpoj_present = False
        self.hplip_present = False
        self.have_dependencies = {}
        self.cups11 = False
        self.hpijs_build = False
        self.ppd_dir = None
        self.drv_dir = None
        self.distros = {}
        self.logoff_required = False
        self.restart_required = False
        self.network_connected = False
        
        self.plugin_path = os.path.join(prop.home_dir, "data", "plugin")
        self.plugin_version = '0.0.0'
        self.plugin_name = ''
        
        
        self.FIELD_TYPES = {
            'distros' : TYPE_LIST,
            'index' : TYPE_INT,
            'versions' : TYPE_LIST,
            'display_name' : TYPE_STRING,
            'alt_names': TYPE_LIST,
            'display': TYPE_BOOL,
            'notes': TYPE_STRING,
            'package_mgrs': TYPE_LIST,
            'package_mgr_cmd':TYPE_STRING,
            'pre_install_cmd': TYPE_LIST,
            'pre_depend_cmd': TYPE_LIST,
            'post_depend_cmd': TYPE_LIST,
            'hpoj_remove_cmd': TYPE_STRING,
            'hplip_remove_cmd': TYPE_STRING,
            'su_sudo': TYPE_STRING,
            'ppd_install': TYPE_STRING,
            'udev_mode_fix': TYPE_BOOL,
            'ppd_dir': TYPE_STRING,
            'drv_dir' : TYPE_STRING,
            'fix_ppd_symlink': TYPE_BOOL,
            'code_name': TYPE_STRING,
            'supported': TYPE_BOOL, # Supported by installer 
            'release_date': TYPE_STRING,
            'packages': TYPE_LIST,
            'commands': TYPE_LIST,
            'same_as_version' : TYPE_STRING,
            'gui_supported' : TYPE_BOOL,
            'scan_supported' : TYPE_BOOL,
            'fax_supported' : TYPE_BOOL,
            'pcard_supported' : TYPE_BOOL,
            'network_supported' : TYPE_BOOL,
            'parallel_supported' : TYPE_BOOL,
            'usb_supported' : TYPE_BOOL,
            'packaged_version': TYPE_STRING, # Version of HPLIP pre-packaged in distro
            'cups_path_with_bitness' : TYPE_BOOL,
        }

        # components
        # 'name': ('description', [<option list>])
        self.components = {
            'hplip': ("HP Linux Imaging and Printing System", ['base', 'network', 'gui', 'fax', 'scan', 'parallel', 'docs']),
            'hpijs': ("HP IJS Printer Driver", ['hpijs', 'hpijs-cups'])
        }

        self.selected_component = 'hplip'

        # options
        # name: (<required>, "<display_name>", [<dependency list>]), ...
        self.options = { 
            'base':     (True,  'Required HPLIP base components', []), # HPLIP
            'network' : (False, 'Network/JetDirect I/O', []),
            'gui' :     (False, 'Graphical User Interfaces (GUIs)', []),
            'fax' :     (False, 'PC Send Fax support', []),
            'scan':     (False, 'Scanning support', []),
            'parallel': (False, 'Parallel I/O (LPT)', []),
            'docs':     (False, 'HPLIP documentation (HTML)', []),

            # hpijs only
            'hpijs':       (True,  'Required HPIJS base components', []),
            'hpijs-cups' : (False, 'CUPS support for HPIJS', []),
        }


        # holds whether the user has selected (turned on each option)
        # initial values are defaults (for GUI only)
        self.selected_options = {
            'base':        True,
            'network':     True,
            'gui':         True,
            'fax':         True,
            'scan':        True,
            'parallel':    False,
            'docs':        True,

            # hpijs only
            'hpijs':       True,
            'hpijs-cups' : True,
        }

        # dependencies
        # 'name': (<required for option>, [<option list>], <display_name>, <check_func>, <runtime/compiletime>), ...
        # Note: any change to the list of dependencies must be reflected in base/distros.py
        self.dependencies = {
            # Required base packages
            'libjpeg':          (True,  ['base', 'hpijs'], "libjpeg - JPEG library", self.check_libjpeg, DEPENDENCY_RUN_AND_COMPILE_TIME),
            'libtool':          (True,  ['base'], "libtool - Library building support services", self.check_libtool, DEPENDENCY_COMPILE_TIME),
            'cups' :            (True,  ['base', 'hpijs-cups'], 'cups - Common Unix Printing System', self.check_cups, DEPENDENCY_RUN_TIME), 
            'cups-devel':       (True,  ['base'], 'cups-devel- Common Unix Printing System development files', self.check_cups_devel, DEPENDENCY_COMPILE_TIME),
            'gcc' :             (True,  ['base', 'hpijs'], 'gcc - GNU Project C and C++ Compiler', self.check_gcc, DEPENDENCY_COMPILE_TIME),
            'make' :            (True,  ['base', 'hpijs'], "make - GNU make utility to maintain groups of programs", self.check_make, DEPENDENCY_COMPILE_TIME),
            'python-devel' :    (True,  ['base'], "python-devel - Python development files", self.check_python_devel, DEPENDENCY_COMPILE_TIME),
            'libpthread' :      (True,  ['base'], "libpthread - POSIX threads library", self.check_libpthread, DEPENDENCY_RUN_AND_COMPILE_TIME),
            'python2x':         (True,  ['base'], "Python 2.2 or greater - Python programming language", self.check_python2x, DEPENDENCY_RUN_AND_COMPILE_TIME),
            'gs':               (True,  ['base', 'hpijs'], "GhostScript - PostScript and PDF language interpreter and previewer", self.check_gs, DEPENDENCY_RUN_TIME),
            'libusb':           (True,  ['base'], "libusb - USB library", self.check_libusb, DEPENDENCY_RUN_AND_COMPILE_TIME),
            


            # Optional base packages
            'cups-ddk':          (False, ['base'], "cups-ddk - CUPS driver development kit", self.check_cupsddk, DEPENDENCY_RUN_TIME), # req. for .drv PPD installs

            # Required scan packages
            'sane':             (True,  ['scan'], "SANE - Scanning library", self.check_sane, DEPENDENCY_RUN_TIME),
            'sane-devel' :      (True,  ['scan'], "SANE - Scanning library development files", self.check_sane_devel, DEPENDENCY_COMPILE_TIME),

            # Optional scan packages
            'xsane':            (False, ['scan'], "xsane - Graphical scanner frontend for SANE", self.check_xsane, DEPENDENCY_RUN_TIME),
            'scanimage':        (False, ['scan'], "scanimage - Shell scanning program", self.check_scanimage, DEPENDENCY_RUN_TIME),
            'pil':              (False, ['scan'], "PIL - Python Imaging Library (required for commandline scanning with hp-scan)", self.check_pil, DEPENDENCY_RUN_TIME), 

            # Required fax packages
            'python23':         (True,  ['fax'], "Python 2.3 or greater - Required for fax functionality", self.check_python23, DEPENDENCY_RUN_TIME),
            'dbus':             (True,  ['fax'], "dbus - Message bus system", self.check_dbus, DEPENDENCY_RUN_AND_COMPILE_TIME),
            'python-dbus':      (True,  ['fax'], "python-dbus - Python bindings for dbus", self.check_python_dbus, DEPENDENCY_RUN_TIME),
            'python-ctypes':    (True,  ['fax'], "python-ctypes - A foreign function library for Python", self.check_python_ctypes, DEPENDENCY_RUN_TIME),

            # Optional fax packages
            'reportlab':        (False, ['fax'], "Reportlab - PDF library for Python", self.check_reportlab, DEPENDENCY_RUN_TIME), 

            # Required parallel I/O packages
            'ppdev':            (True,  ['parallel'], "ppdev - Parallel port support kernel module.", self.check_ppdev, DEPENDENCY_RUN_TIME),

            # Required gui packages
            'pyqt':             (True,  ['gui'], "PyQt - Qt interface for Python", self.check_pyqt, DEPENDENCY_RUN_TIME), # PyQt 3.x

            # Required network I/O packages
            'libnetsnmp-devel': (True,  ['network'], "libnetsnmp-devel - SNMP networking library development files", self.check_libnetsnmp, DEPENDENCY_RUN_AND_COMPILE_TIME),
            'libcrypto':        (True,  ['network'], "libcrypto - OpenSSL cryptographic library", self.check_libcrypto, DEPENDENCY_RUN_AND_COMPILE_TIME),
        }

        for opt in self.options:
            update_spinner()
            for d in self.dependencies:
                if opt in self.dependencies[d][1]:
                    self.options[opt][2].append(d)

        self.load_distros()
        
        #for d in self.distros:
        #    print
##        import pprint
##        print "6: ", pprint.pprint(self.distros['fedora']['versions']['6'])
##        print
##        print "6.0: ", pprint.pprint(self.distros['fedora']['versions']['6.0'])
##        sys.exit(1)

        self.distros_index = {}
        for d in self.distros:
            self.distros_index[self.distros[d]['index']] = d        


    def init(self, callback=None):
        if callback is not None:
            callback("Init...\n")

        update_spinner()

        # Package manager names
        self.package_mgrs = []
        for d in self.distros:
            update_spinner()

            for a in self.distros[d].get('package_mgrs', []):
                if a and a not in self.package_mgrs:
                    self.package_mgrs.append(a)

        self.version_description, self.version_public, self.version_internal = self.get_hplip_version()
        log.debug("HPLIP Description=%s Public version=%s Internal version = %s"  % 
            (self.version_description, self.version_public, self.version_internal))

        # have_dependencies
        # is each dependency satisfied?
        # start with each one 'No'
        for d in self.dependencies:
            update_spinner()
            self.have_dependencies[d] = False

        self.get_distro()

        if callback is not None:
            callback("Distro: %s\n" % self.distro)

        self.check_dependencies(callback)

        for d in self.dependencies:
            update_spinner()

            log.debug("have %s = %d" % (d, self.have_dependencies[d]))

            if callback is not None:
                callback("Result: %s = %d\n" % (d, self.have_dependencies[d]))

        pid, cmdline = self.check_pkg_mgr()
        if pid:
            log.debug("Running package manager: %s (%d)" % (cmdline, pid) )

        self.bitness = utils.getBitness()
        log.debug("Bitness = %d" % self.bitness)

        update_spinner()

        self.endian = utils.getEndian()
        log.debug("Endian = %d" % self.endian)

        update_spinner()

        self.distro_name = self.distros_index[self.distro]
        self.distro_version_supported = self.get_distro_ver_data('supported', False)

        log.debug("Distro = %s Distro Name = %s Display Name= %s Version = %s Supported = %s" % 
            (self.distro, self.distro_name, self.distros[self.distro_name]['display_name'], 
             self.distro_version, self.distro_version_supported))

        self.hpoj_present = self.check_hpoj()
        log.debug("HPOJ = %s" % self.hpoj_present)

        update_spinner()

        self.hplip_present = self.check_hplip()
        log.debug("HPLIP (prev install) = %s" % self.hplip_present)

        status, output = self.run('cups-config --version')
        self.cups_ver = output.strip()
        log.debug("CUPS version = %s" % self.cups_ver)

        self.cups11 = output.startswith('1.1')
        log.debug("Is CUPS 1.1.x? %s" % self.cups11)

        status, self.sys_uname_info = self.run('uname -a')
        self.sys_uname_info = self.sys_uname_info.replace('\n', '')
        log.debug(self.sys_uname_info)

        self.distro_changed()

        # Record the installation time/date and version.
        # Also has the effect of making the .hplip.conf file user r/w
        # on the 1st run so that running hp-setup as root doesn't lock
        # the user out of owning the file
        user_cfg.installation.date_time = time.strftime("%x %H:%M:%S", time.localtime())
        user_cfg.installation.version = self.version_public

        if callback is not None:
            callback("Done")


    def init_for_docs(self, distro_name, version, bitness=32):
        self.distro_name = distro_name
        self.distro_version = version

        try:
            self.distro = self.distros[distro_name]['index']
        except KeyError:
            log.error("Invalid distro name: %s" % distro_name)
            sys.exit(1)

        self.bitness = bitness

        for d in self.dependencies:
            self.have_dependencies[d] = True

        self.enable_ppds = self.get_distro_ver_data('ppd_install', 'ppd') == 'ppd'
        self.ppd_dir = self.get_distro_ver_data('ppd_dir')
        self.drv_dir = self.get_distro_ver_data('drv_dir')

        self.distro_version_supported = True # for manual installs    


    def check_dependencies(self, callback=None):
        update_ld_output()

        for d in self.dependencies:
            update_spinner()

            log.debug("Checking for dependency '%s'...\n" % d)

            if callback is not None:
                callback("Checking: %s\n" % d)

            self.have_dependencies[d] = self.dependencies[d][3]()
            log.debug("have %s = %d" % (d, self.have_dependencies[d]))

        cleanup_spinner()


    def password_func(self):
        if self.password:
            return self.password
        elif self.ui_mode == INTERACTIVE_MODE:
            import getpass
            return getpass.getpass("Enter password: ")
        else:
            return ''


    def run(self, cmd, callback=None, timeout=300):
        if cmd is None: 
            return 1, ''
        output = cStringIO.StringIO()
        ok, ret = False, ''
        # Hack! TODO: Fix!
        check_timeout = not (cmd.startswith('xterm') or cmd.startswith('gnome-terminal'))

        try:
            child = pexpect.spawn(cmd, timeout=1)
        except pexpect.ExceptionPexpect:
            return 1, ''

        try:
            try:
                start = time.time()

                while True:
                    update_spinner()

                    i = child.expect_list(PASSWORD_EXPECT_LIST)

                    cb = child.before
                    if cb:
                        # output
                        start = time.time()
                        log.log_to_file(cb)
                        log.debug(cb)
                        output.write(cb)

                        if callback is not None:
                            if callback(cb): # cancel
                                break

                    elif check_timeout:
                        # no output
                        span = int(time.time()-start)

                        if span:
                            if span % 5 == 0:
                                log.debug("No output seen in %d secs" % span)

                            if span > timeout:
                                log.error("No output seen in over %d sec... (Is the CD-ROM/DVD source repository enabled? It shouldn't be!)" % timeout)
                                child.close()
                                child.terminate(force=True)
                                break

                    if i == 0: # EOF
                        ok, ret = True, output.getvalue()
                        break

                    elif i == 1: # TIMEOUT
                        continue

                    else: # password
                        child.sendline(self.password)

            except (Exception, pexpect.ExceptionPexpect):
                log.exception()

        finally:
            cleanup_spinner()

            try:
                child.close()
            except OSError:
                pass

        if ok:        
            return child.exitstatus, ret
        else:
            return 1, ''


    def get_distro(self):
        log.debug("Determining distro...")
        self.distro, self.distro_version = DISTRO_UNKNOWN, '0.0'

        found = False

        lsb_release = utils.which("lsb_release")

        if lsb_release:
            log.debug("Using 'lsb_release -is/-rs'")
            cmd = os.path.join(lsb_release, "lsb_release")
            status, name = self.run(cmd + ' -is')
            name = name.lower().strip()
            log.debug("Distro name=%s" % name)

            if not status and name:
                status, ver = self.run(cmd + ' -rs')
                ver = ver.lower().strip()
                log.debug("Distro version=%s" % ver)

                if not status and ver:
                    for d in self.distros:
                        if name.find(d) > -1:
                            self.distro = self.distros[d]['index']
                            found = True
                            self.distro_version = ver
                            break

        if not found:
            try:
                name = file('/etc/issue', 'r').read().lower().strip()
            except IOError:
                # Some O/Ss don't have /etc/issue (Mac)
                self.distro, self.distro_version = DISTRO_UNKNOWN, '0.0'
            else:
                for d in self.distros:
                    if name.find(d) > -1:
                        self.distro = self.distros[d]['index']
                        found = True
                    else:
                        for x in self.distros[d].get('alt_names', ''):
                            if x and name.find(x) > -1:
                                self.distro = self.distros[d]['index']
                                found = True
                                break

                    if found:
                        break

                if found:
                    for n in name.split(): 
                        m= n
                        if '.' in n:
                            m = '.'.join(n.split('.')[:2])

                        try:
                            float(m)
                        except ValueError:
                            try:
                                int(m)
                            except ValueError:
                                self.distro_version = '0.0'
                            else:
                                self.distro_version = m
                                break
                        else:
                            self.distro_version = m
                            break

                    log.debug("/etc/issue: %s %s" % (name, self.distro_version))

        log.debug("distro=%d, distro_version=%s" % (self.distro, self.distro_version))


    def distro_changed(self):
        ppd_install = self.get_distro_ver_data('ppd_install', 'ppd')

        if ppd_install not in ('ppd', 'drv'):
            log.warning("Invalid ppd_install value: %s" % ppd_install)

        if self.cups11:
            self.enable_ppds = True
        else:
            self.enable_ppds = (ppd_install == 'ppd')

        log.debug("Enable PPD install: %s (False=drv)" % self.enable_ppds)

        self.ppd_dir = self.get_distro_ver_data('ppd_dir')

        if not self.ppd_dir: 
            log.warning("Invalid ppd_dir value: %s" % self.ppd_dir)

        self.drv_dir = self.get_distro_ver_data('drv_dir')
        if not self.enable_ppds and not self.drv_dir: 
            log.warning("Invalid drv_dir value: %s" % self.drv_dir)

        self.distro_version_supported = self.get_distro_ver_data('supported', False)
        self.selected_options['fax'] = self.get_distro_ver_data('fax-supported', True)
        self.selected_options['gui'] = self.get_distro_ver_data('gui-supported', True)
        self.selected_options['network'] = self.get_distro_ver_data('network-supported', True)
        self.selected_options['scan'] = self.get_distro_ver_data('scan-supported', True)
        self.selected_options['parallel'] = self.get_distro_ver_data('parallel-supported', False)
                

    def __fixup_data(self, key, data):
        field_type = self.FIELD_TYPES.get(key, TYPE_STRING)
        #log.debug("%s (%s) %d" % (key, data, field_type))
        
        if field_type == TYPE_BOOL:
            return utils.to_bool(data)

        elif field_type == TYPE_STRING:
            if type('') == type(data):
                return data.strip()
            else:
                return data

        elif field_type == TYPE_INT:
            try:
                return int(data)
            except ValueError:
                return 0

        elif field_type == TYPE_LIST:
            return [x for x in data.split(',') if x]


    def load_distros(self):
        if self.mode  == MODE_INSTALLER:
            distros_dat_file = os.path.join('installer', 'distros.dat')

        elif self.mode == MODE_CREATE_DOCS:
            distros_dat_file = os.path.join('..', '..', 'installer', 'distros.dat')

        else: # MODE_CHECK
            distros_dat_file = os.path.join(prop.home_dir, 'installer', 'distros.dat')

            if not os.path.exists(distros_dat_file):
                log.debug("DAT file not found at %s. Using local relative path..." % distros_dat_file)
                distros_dat_file = os.path.join('installer', 'distros.dat')

        distros_dat = Config(distros_dat_file, True)
        distros_list = self.__fixup_data('distros', distros_dat.distros.distros)
        log.debug(distros_list)

        for distro in distros_list:
            update_spinner()
            d = {}
            try:
                distro_section = distros_dat[distro]
            except KeyError:
                log.debug("Missing distro section in distros.dat: [%s]" % distro)
                continue

            for key in distro_section:
                d[key] = self.__fixup_data(key, distro_section[key])

            self.distros[distro] = d
            versions = self.__fixup_data("versions", distros_dat[distro]['versions'])
            self.distros[distro]['versions'] = {}

            for ver in versions:
                v = {}
                try:
                    ver_section = distros_dat["%s:%s" % (distro, ver)]
                except KeyError:
                    log.debug("Missing version section in distros.dat: [%s:%s]" % (distro, ver))
                    continue

                for key in ver_section:
                    v[key] = self.__fixup_data(key, ver_section[key])
                
                self.distros[distro]['versions'][ver] = v
                self.distros[distro]['versions'][ver]['dependency_cmds'] = {}

                for dep in self.dependencies:
                    dd = {}
                    try:
                        dep_section = distros_dat["%s:%s:%s" % (distro, ver, dep)].copy()
                    except KeyError:
                        log.debug("Missing dependency section in distros.dat: [%s:%s:%s]" % (distro, ver, dep))
                        continue


                    for key in dep_section:
                        dd[key] = self.__fixup_data(key, dep_section[key])
                    
                    self.distros[distro]['versions'][ver]['dependency_cmds'][dep] = dd
            
            versions = self.distros[distro]['versions']
            for ver in versions:
                ver_section = distros_dat["%s:%s" % (distro, ver)]
                
                if 'same_as_version' in ver_section:
                    v = self.__fixup_data("same_as_version", ver_section['same_as_version'])
                    log.debug("Setting %s:%s to %s:%s" % (distro, ver, distro, v))

                    try:
                        vv = self.distros[distro]['versions'][v].copy()
                        vv['same_as_version'] = v
                        self.distros[distro]['versions'][ver] = vv
                    except KeyError:
                        log.debug("Missing 'same_as_version=' version in distros.dat for section [%s:%s]." % (distro, v))
                        continue
                
            
    def pre_install(self):
        pass


    def pre_depend(self):
        pass


    def check_python2x(self):
        py_ver = sys.version_info
        py_major_ver, py_minor_ver = py_ver[:2]
        log.debug("Python ver=%d.%d" % (py_major_ver, py_minor_ver))
        return py_major_ver >= 2


    def check_gcc(self):
        return check_tool('gcc --version', 0) and check_tool('g++ --version', 0)


    def check_make(self):
        return check_tool('make --version', 3.0)


    def check_libusb(self):
        if not check_lib('libusb'):
            return False

        return len(locate_file_contains("usb.h", '/usr/include', 'usb_init(void)'))


    def check_libjpeg(self):
        return check_lib("libjpeg") and check_file("jpeglib.h")


    def check_libcrypto(self):
        return check_lib("libcrypto") and check_file("crypto.h")


    def check_libpthread(self):
        return check_lib("libpthread") and check_file("pthread.h")


    def check_libnetsnmp(self):
        return check_lib("libnetsnmp") and check_file("net-snmp-config.h")


    def check_reportlab(self):
        try:
            log.debug("Trying to import 'reportlab'...")
            import reportlab

            ver = reportlab.Version
            try:
                ver_f = float(ver)
            except ValueError:
                log.debug("Can't determine version.")
                return False
            else:
                log.debug("Version: %.1f" % ver_f)
                if ver_f >= 2.0:
                    log.debug("Success.")
                    return True
                else:
                    return False

        except ImportError:
            log.debug("Failed.")
            return False


    def check_python23(self):
        py_ver = sys.version_info
        py_major_ver, py_minor_ver = py_ver[:2]
        log.debug("Python ver=%d.%d" % (py_major_ver, py_minor_ver))
        return py_major_ver >= 2 and py_minor_ver >= 3


    def check_sane(self):
        return check_lib('libsane')


    def check_sane_devel(self):
        return len(locate_file_contains("sane.h", '/usr/include', 'extern SANE_Status sane_init'))


    def check_xsane(self):
        if os.getenv('DISPLAY'):
            return check_tool('xsane --version', 0.9) # will fail if X not running...
        else:
            return bool(utils.which("xsane")) # ...so just see if it installed somewhere


    def check_scanimage(self):
        return check_tool('scanimage --version', 1.0)


    def check_ppdev(self):
        return check_lsmod('ppdev')


    def check_gs(self):
        return check_tool('gs -v', 7.05)


    def check_pyqt(self):
        try:
            import qt
            pyqtVersion = None
            try:
                pyqtVersion = qt.PYQT_VERSION_STR
                log.debug("PYQT_VERSION_STR = %s" % pyqtVersion)
            except AttributeError:
                try:
                    pyqtVersion = qt.PYQT_VERSION
                    log.debug("PYQT_VERSION = %s" % pyqtVersion)
                except AttributeError:
                    pass

            if pyqtVersion is not None:
                while pyqtVersion.count('.') < 2:
                    pyqtVersion += '.0'

                (maj_ver, min_ver, pat_ver) = pyqtVersion.split('.')

                if pyqtVersion.find('snapshot') >= 0:
                    log.debug("A non-stable snapshot version of PyQt is installed.")
                    pass
                else:    
                    try:
                        maj_ver = int(maj_ver)
                        min_ver = int(min_ver)
                        pat_ver = int(pat_ver)
                    except ValueError:
                        maj_ver, min_ver, pat_ver = 0, 0, 0
                    else:
                        log.debug("Version %d.%d.%d installed." % (maj_ver, min_ver, pat_ver))

                    if maj_ver < MINIMUM_PYQT_MAJOR_VER or \
                        (maj_ver == MINIMUM_PYQT_MAJOR_VER and min_ver < MINIMUM_PYQT_MINOR_VER):
                        log.debug("HPLIP may not function properly with the version of PyQt that is installed (%d.%d.%d)." % (maj_ver, min_ver, pat_ver))
                        log.debug("Incorrect version of PyQt installed. Ver. %d.%d or greater required." % (MINIMUM_PYQT_MAJOR_VER, MINIMUM_PYQT_MINOR_VER))
                        return True
                    else:
                        return True

        except ImportError:
             return False


    def check_python_devel(self):
        return check_file('Python.h')


    def check_python_dbus(self):
        log.debug("Checking for python-dbus (>= 0.80)...")
        try:
            import dbus
            try:
                ver = dbus.version
                log.debug("Version: %s" % '.'.join([str(x) for x in dbus.version]))
                return ver >= (0,80,0)
            
            except AttributeError:
                try:
                    ver = dbus.__version__
                    log.debug("Version: %s" % dbus.__version__)
                    log.debug("HPLIP requires dbus version > 0.80.")
                    return False
                
                except AttributeError:
                    log.debug("Unknown version. HPLIP requires dbus version > 0.80.")
                    return False
        
        except ImportError:
            return False
            
    
    def check_python_ctypes(self):
        try:
            import ctypes
            return True
        except ImportError:
            return False


    def check_dbus(self):
        log.debug("Checking for dbus running...")
        return check_ps(['dbus-daemon']) and \
            len(locate_file_contains("dbus-message.h", '/usr/include', 'dbus_message_new_signal'))


    def check_cups_devel(self):
        return check_file('cups.h') and bool(utils.which('lpr'))


    def check_cups(self):
        status, output = self.run('lpstat -r')
        if status > 0:
            log.debug("CUPS is not running.")
            return False
        else:
            log.debug("CUPS is running.")
            return True


    def check_hpoj(self):
        log.debug("Checking for 'HPOJ'...")
        return check_ps(['ptal-mlcd', 'ptal-printd', 'ptal-photod']) or \
            bool(utils.which("ptal-init"))


    def check_hplip(self):
        log.debug("Checking for HPLIP (pre-2.x)...")
        return check_ps(['hpiod', 'hpssd']) and locate_files('hplip.conf', '/etc/hp')


    def check_hpssd(self):
        log.debug("Checking for hpssd...")
        return check_ps(['hpssd'])


    def check_libtool(self):
        log.debug("Checking for libtool...")
        return check_tool('libtool --version')


    def check_pil(self):
        log.debug("Checking for PIL...")
        try:
            import Image
            return True
        except ImportError:
            return False


    def check_cupsddk(self):
        log.debug("Checking for cups-ddk...")
        # TODO: Compute these paths some way or another...
        #return check_tool("/usr/lib/cups/driver/drv list") and os.path.exists("/usr/share/cupsddk/include/media.defs")
        return check_file('drv', "/usr/lib/cups/driver") and check_file('media.defs', "/usr/share/cupsddk/include")        

    def check_pkg_mgr(self):
        """
            Check if any pkg mgr processes are running
        """
        log.debug("Searching for '%s' in running processes..." % self.package_mgrs)

        processes = get_process_list()
        
        for pid, cmdline in processes:
            for p in self.package_mgrs:
                if p in cmdline:
                    for k in OK_PROCESS_LIST:
                        if k not in cmdline:
                            log.debug("Found: %s (%d)" % (cmdline, pid))
                            return (pid, cmdline)
        
        log.debug("Not found")
        return (0, '')
        

    def get_hplip_version(self):
        self.version_description, self.version_public, self.version_internal = '', '', ''

        if self.mode == MODE_INSTALLER:
            ac_init_pat = re.compile(r"""AC_INIT\(\[(.*?)\], *\[(.*?)\], *\[(.*?)\], *\[(.*?)\] *\)""", re.IGNORECASE)

            try:
                config_in = open('./configure.in', 'r')
            except IOError:
                self.version_description, self.version_public, self.version_internal = \
                    '', sys_cfg.configure['internal-tag'], sys_cfg.hplip.version
            else:
                for c in config_in:
                    if c.startswith("AC_INIT"):
                        match_obj = ac_init_pat.search(c)
                        self.version_description = match_obj.group(1)
                        self.version_public = match_obj.group(2)
                        self.version_internal = match_obj.group(3)
                        name = match_obj.group(4)
                        break

                config_in.close()

                if name != 'hplip':
                    log.error("Invalid archive!")


        else: # MODE_CHECK
            try:
                self.version_description, self.version_public, self.version_internal = \
                    '', sys_cfg.configure['internal-tag'], sys_cfg.hplip.version
            except KeyError:
                self.version_description, self.version_public, self.version_internal = '', '', ''

        return self.version_description, self.version_public, self.version_internal            


    def configure(self): 
        configure_cmd = './configure'
        
        dbus_avail = self.have_dependencies['dbus'] and self.have_dependencies['python-dbus']

        if self.selected_options['network']:
            configure_cmd += ' --enable-network-build'
        else:
            configure_cmd += ' --disable-network-build'

        if self.selected_options['parallel']:
            configure_cmd += ' --enable-pp-build'
        else:
            configure_cmd += ' --disable-pp-build'

        if self.selected_options['fax'] and dbus_avail:
            configure_cmd += ' --enable-fax-build'
        else:
            configure_cmd += ' --disable-fax-build'
            
        if dbus_avail:
            configure_cmd += ' --enable-dbus-build'
        else:
            configure_cmd += ' --disable-dbus-build'

        if self.selected_options['gui']:
            configure_cmd += ' --enable-gui-build'
        else:
            configure_cmd += ' --disable-gui-build'

        if self.selected_options['scan']:
            configure_cmd += ' --enable-scan-build'
        else:
            configure_cmd += ' --disable-scan-build'

        if self.selected_options['docs']:
            configure_cmd += ' --enable-doc-build'
        else:
            configure_cmd += ' --disable-doc-build'

        if self.enable_ppds: # Use ppd install if cups 1.1 or ppd_install=ppd
            configure_cmd += ' --enable-foomatic-ppd-install --disable-foomatic-drv-install'

        else: # otherwise, use drv if cups ddk is avail, otherwise fall back to .ppds

            if self.have_dependencies['cups-ddk']:
                configure_cmd += ' --disable-foomatic-ppd-install --enable-foomatic-drv-install'

                if self.drv_dir is not None:
                    configure_cmd += ' --with-drvdir=%s' % self.drv_dir

            else:
                configure_cmd += ' --enable-foomatic-ppd-install --disable-foomatic-drv-install'

        if self.ppd_dir is not None:
            configure_cmd += ' --with-hpppddir=%s' % self.ppd_dir

        if self.hpijs_build:
            configure_cmd += ' --enable-hpijs-only-build'
        else:
            configure_cmd += ' --disable-hpijs-only-build'

        if self.bitness == 64:
            configure_cmd += ' --libdir=/usr/lib64'

        configure_cmd += ' --prefix=%s' % self.install_location

        if self.cups11:
            configure_cmd += ' --enable-cups11-build'
            
        if self.get_distro_ver_data('cups_path_with_bitness', False) and self.bitness == 64:
            configure_cmd += ' --with-cupsbackenddir=/usr/lib64/cups/backend --with-cupsfilterdir=/usr/lib64/cups/filter'

        return configure_cmd


    def restart_cups(self):
        if os.path.exists('/etc/init.d/cups'):
            cmd = self.su_sudo() % '/etc/init.d/cups restart'

        elif os.path.exists('/etc/init.d/cupsys'):
            cmd = self.su_sudo() % '/etc/init.d/cupsys restart'

        else:
            cmd = self.su_sudo() % 'killall -HUP cupsd'

        self.run(cmd)


    def stop_hplip(self):
        return self.su_sudo() % "/etc/init.d/hplip stop"


    def su_sudo(self):
        if os.geteuid() == 0:
            return '%s'
        else:
            try:
                cmd = self.distros[self.distro_name]['su_sudo']
            except KeyError:
                cmd = 'su'

            if cmd == 'su':
                return 'su -c "%s"'
            else:
                return 'sudo %s'

    def su_sudo_str(self):
        return self.get_distro_data('su_sudo', 'su')


    def build_cmds(self): 
        return [self.configure(), 
                'make clean', 
                'make', 
                self.su_sudo() % 'make install']


    def get_distro_ver_data(self, key, default=None):
        try:
            return self.distros[self.distro_name]['versions'][self.distro_version].get(key, None) or \
                self.distros[self.distro_name].get(key, None) or default
        except KeyError:
            return default

        return value


    def get_distro_data(self, key, default=None):
        try:
            return self.distros[self.distro_name].get(key, None) or default
        except KeyError:
            return default


    def get_ver_data(self, key, default=None):
        try:
            return self.distros[self.distro_name]['versions'][self.distro_version].get(key, None) or default
        except KeyError:
            return default

        return value


    def get_dependency_data(self, dependency):
        dependency_cmds = self.get_ver_data("dependency_cmds", {})
        dependency_data = dependency_cmds.get(dependency, {})
        packages = dependency_data.get('packages', [])
        commands = dependency_data.get('commands', [])
        return packages, commands


    def get_dependency_commands(self):
        dd = self.dependencies.keys()
        dd.sort()
        commands_to_run = []
        packages_to_install = []
        overall_commands_to_run = []
        for d in dd:
            include = False
            for opt in self.dependencies[d][1]:
                if self.selected_options[opt]:
                    include = True
            if include:
                pkgs, cmds = self.get_dependency_data(d)

                if pkgs:
                    packages_to_install.extend(pkgs)

                if cmds:
                    commands_to_run.extend(cmds)

        package_mgr_cmd = self.get_distro_data('package_mgr_cmd')

        overall_commands_to_run.extend(commands_to_run)

        if package_mgr_cmd:
            packages_to_install = ' '.join(packages_to_install)
            overall_commands_to_run.append(utils.cat(package_mgr_cmd))

        if not overall_commands_to_run:
            log.error("No cmds/pkgs")
            
        return overall_commands_to_run


    def distro_known(self):
        return self.distro != DISTRO_UNKNOWN and self.distro_version != DISTRO_VER_UNKNOWN


    def distro_supported(self):
        if self.mode == MODE_INSTALLER:
            return self.distro != DISTRO_UNKNOWN and self.distro_version != DISTRO_VER_UNKNOWN and self.get_ver_data('supported', False)
        else:
            return True # For docs (manual install)


    def sort_vers(self, x, y):
        try:
            return cmp(float(x), float(y))
        except ValueError:
            return cmp(x, y)


    def running_as_root(self):
        return os.geteuid() == 0


    def show_release_notes_in_browser(self):
        url = "file://%s" % os.path.join(os.getcwd(), 'doc', 'release_notes.html')
        log.debug(url)
        status, output = self.run("xhost +")
        utils.openURL(url)


    def count_num_required_missing_dependencies(self):
        num_req_missing = 0
        for d, desc, opt in self.missing_required_dependencies():
            num_req_missing += 1
        return num_req_missing


    def count_num_optional_missing_dependencies(self):
        num_opt_missing = 0
        for d, desc, req, opt in self.missing_optional_dependencies():
            num_opt_missing += 1
        return num_opt_missing


    def missing_required_dependencies(self): # missing req. deps in req. options
        for opt in self.components[self.selected_component][1]:
            if self.options[opt][0]: # required options
                for d in self.options[opt][2]: # dependencies for option
                    if self.dependencies[d][0]: # required option
                        if not self.have_dependencies[d]: # missing
                            log.debug("Missing required dependency: %s" % d)
                            yield d, self.dependencies[d][2], opt
                            # depend, desc, option


    def missing_optional_dependencies(self):
        # missing deps in opt. options

        for opt in self.components[self.selected_component][1]:
            if not self.options[opt][0]: # not required option
                if self.selected_options[opt]: # only for options that are ON
                    for d in self.options[opt][2]: # dependencies
                        if not self.have_dependencies[d]: # missing dependency
                            log.debug("Missing optional dependency: %s" % d)
                            yield d, self.dependencies[d][2], self.dependencies[d][0], opt
                            # depend, desc, required_for_opt, opt

        # opt. deps in req. options
        for opt in self.components[self.selected_component][1]:
              if self.options[opt][0]: # required options
                  for d in self.options[opt][2]: # dependencies for option
                      if not self.dependencies[d][0]: # optional dep
                          if not self.have_dependencies[d]: # missing
                              log.debug("Missing optional dependency: %s" % d)
                              yield d, self.dependencies[d][2], self.dependencies[d][0], opt
                              # depend, desc, option  


    def select_options(self, answer_callback):
        num_opt_missing = 0
        # not-required options
        for opt in self.components[self.selected_component][1]:
            if not self.options[opt][0]: # not required
                self.selected_options[opt] = answer_callback(opt, self.options[opt][1])

                if self.selected_options[opt]: # only for options that are ON
                    for d in self.options[opt][2]: # dependencies
                        if not self.have_dependencies[d]: # missing dependency
                            log.debug("Missing optional dependency: %s" % d)
                            num_opt_missing += 1

        return num_opt_missing


    def check_network_connection(self):
        self.network_connected = False

        wget = utils.which("wget")
        if wget:
            wget = os.path.join(wget, "wget")
            cmd = "%s --timeout=10 %s" % (wget, HTTP_GET_TARGET)
            log.debug(cmd)
            status, output = self.run(cmd)
            log.debug("wget returned: %d" % status)
            self.network_connected = (status == 0)

        else:
            curl = utils.which("curl")
            if curl:
                curl = os.path.join(curl, "curl")
                cmd = "%s --connect-timeout 5 --max-time 10 %s" % (curl, HTTP_GET_TARGET)
                log.debug(cmd)
                status, output = self.run(cmd)
                log.debug("curl returned: %d" % status)
                self.network_connected = (status == 0)

            else:
                ping = utils.which("ping")

                if ping:
                    ping = os.path.join(ping, "ping")
                    cmd = "%s -c1 -W1 -w10 %s" % (ping, PING_TARGET)
                    log.debug(cmd)
                    status, output = self.run(cmd)
                    log.debug("ping returned: %d" % status)
                    self.network_connected = (status == 0)

        return self.network_connected


    def run_pre_install(self, callback=None):
        pre_cmd = self.get_distro_ver_data('pre_install_cmd')
        log.debug(pre_cmd)
        if pre_cmd:
            x = 1
            for cmd in pre_cmd:
                status, output = self.run(cmd)

                if status != 0:
                    log.warn("An error occurred running '%s'" % cmd)

                if callback is not None:
                    callback(cmd, "Pre-install step %d" % x)

                x += 1

            return True

        else:
            return False

    def run_pre_depend(self, callback=None):
        pre_cmd = self.get_distro_ver_data('pre_depend_cmd')
        log.debug(pre_cmd)
        if pre_cmd:
            x = 1
            for cmd in pre_cmd:
                status, output = self.run(cmd)

                if status != 0:
                    log.warn("An error occurred running '%s'" % cmd)

                if callback is not None:
                    callback(cmd, "Pre-depend step %d" % x)

                x += 1

    def run_post_depend(self, callback=None):
        post_cmd = self.get_distro_ver_data('post_depend_cmd')
        log.debug(post_cmd)
        if post_cmd:
            x = 1
            for cmd in post_cmd:
                status, output = self.run(cmd)

                if status != 0:
                    log.warn("An error occurred running '%s'" % cmd)

                if callback is not None:
                    callback(cmd, "Post-depend step %d" % x)

                x += 1


    def pre_build(self):
        cmds = []
        if self.get_distro_ver_data('fix_ppd_symlink', False):
            cmds.append(self.su_sudo() % 'python ./installer/fix_symlink.py')

        return cmds

    def run_pre_build(self, callback=None):
        x = 1
        for cmd in self.pre_build():
            status, output = self.run(cmd)
            if callback is not None:
                callback(cmd, "Pre-build step %d"  % x)

            x += 1


    def run_post_build(self, callback=None):
        x = 1
        for cmd in self.post_build():
            status, output = self.run(cmd)
            if callback is not None:
                callback(cmd, "Post-build step %d"  % x)

            x += 1


    def post_build(self):
        cmds = []
        self.logoff_required = False
        self.restart_required = True
        trigger_required = True

        # Restart CUPS if necessary
        if self.cups11:
            cmds.append(self.restart_cups())

        # Kill any running hpssd.py instance from a previous install
        if self.check_hpssd():
            pid = get_ps_pid('hpssd')
            if pid:
                kill = os.path.join(utils.which("kill"), "kill") + " %d" % pid

                cmds.append(self.su_sudo() % kill)

        return cmds


    def logoff(self):
        ok = False
        pkill = utils.which('pkill')
        if pkill:
            cmd = "%s -KILL -u %s" % (os.path.join(pkill, "pkill"), prop.username)
            cmd = self.su_sudo() % cmd
            status, output = self.run(cmd)

            ok = (status == 0)

        return ok


    def restart(self):
        ok = False
        shutdown = utils.which('shutdown')
        if shutdown:
            cmd = "%s -r now" % (os.path.join(shutdown, "shutdown"))
            cmd = self.su_sudo() % cmd
            status, output = self.run(cmd)

            ok = (status == 0)

        return ok


    def check_for_gui_support(self):
        return os.getenv('DISPLAY') and self.selected_options['gui'] and utils.checkPyQtImport()


    def run_hp_setup(self):
        status = 0
        hpsetup = utils.which("hp-setup")

        if self.check_for_gui_support():
            if hpsetup:
                c = 'hp-setup -u --username=%s' % prop.username
            else:
                c = 'python ./setup.py -u --username=%s' % prop.username

            cmd = self.su_sudo() % c
            log.debug(cmd)

            status, output = self.run(cmd)
        else:
            if hpsetup:
                c = "hp-setup -i"
            else:
                c = "python ./setup.py -i"

            cmd = self.su_sudo() % c
            log.debug(cmd)
            os.system(cmd)


        return status == 0


    def remove_hplip(self, callback=None):
        failed = True
        self.stop_pre_2x_hplip(callback)

        hplip_remove_cmd = self.get_distro_data('hplip_remove_cmd')
        if hplip_remove_cmd:
            if callback is not None:
                callback(hplip_remove_cmd, "Removing old HPLIP version")

                status, output = self.run(hplip_remove_cmd)

            if status == 0:
                self.hplip_present = self.check_hplip()

                if not self.hplip_present:
                    failed = False

        return failed


    def stop_pre_2x_hplip(self, callback=None):
        hplip_init_script = '/etc/init.d/hplip stop'
        if os.path.exists(hplip_init_script):
            cmd = self.su_sudo() % hplip_init_script

            if callback is not None:
                callback(cmd, "Stopping old HPLIP version.")

            status, output = self.run(cmd)


    def remove_hpoj(self, callback=None):
        # TODO: Must stop PTAL?
        hpoj_remove_cmd = self.get_distro_data('hpoj_remove_cmd')
        if hpoj_remove_cmd:
            if callback is not None:
                callback(hpoj_remove_cmd, "Removing HPOJ")

                status, output = self.run(hpoj_remove_cmd)

            if status == 0:
                self.hpoj_present = check_hpoj()

                if not self.hpoj_present:
                    failed = False

        return failed


    def check_password(self, password_entry_callback, callback=None):
        self.clear_su_sudo_password()
        x = 1
        while True:
            self.password = password_entry_callback()
            cmd = self.su_sudo() % "true"

            log.debug(cmd)

            status, output = self.run(cmd)

            log.debug(status)
            log.debug(output)

            if status == 0:
                if callback is not None:
                    callback("", "Password accepted")
                return True

            if callback is not None:
                callback("", "Password incorrect. %d attempt(s) left." % (3-x))

            x += 1

            if x > 3:
                return False


    def clear_su_sudo_password(self):
        if self.su_sudo_str() == 'sudo':
            log.debug("Clearing password...")
            self.run("sudo -K")


            
    # PLUGIN HELPERS
    
    def set_plugin_version(self):
        self.plugin_version = '.'.join(sys_cfg.hplip.version.split('.')[:3])
        self.plugin_name = 'hplip-%s-plugin.run' % self.plugin_version
        
    
    def get_plugin_conf_url(self):
        url = "http://hplip.sf.net/plugin.conf"
        
        if os.path.exists('/etc/hp/plugin.conf'):
            url = "file:///etc/hp/plugin.conf"
            
        elif os.path.exists(os.path.join(sys_cfg.dirs.home, 'plugin.conf')):
            url = "file://" + os.path.join(sys_cfg.dirs.home, 'plugin.conf')
            
        log.debug("Plugin.conf url: %s" % url)
        return url
        
        
    def get_plugin_info(self, plugin_conf_url, callback):
        ok, size, checksum, timestamp, url = False, 0, 0, 0.0, ''

        if not self.create_plugin_dir():
            log.error("Could not create plug-in directory.")
            return '', 0, 0, 0, False

        local_conf_fp, local_conf = utils.make_temp_file()
        
        if os.path.exists(local_conf):
            os.remove(local_conf)
        
        try:
            try:
                filename, headers = urllib.urlretrieve(plugin_conf_url, local_conf, callback)
            except IOError, e:
                log.error("I/O Error: %s" % e.strerror)
                return '', 0, 0, 0, False
            
            if not os.path.exists(local_conf):
                log.error("plugin.conf not found.")
                return '', 0, 0, 0, False
            
            plugin_conf_p = ConfigParser.ConfigParser()
            
            try:
                plugin_conf_p.read(local_conf)
            except (ConfigParser.MissingSectionHeaderError, ConfigParser.ParsingError):
                log.error("Error parsing file - 404 error?")
                return '', 0, 0, 0, False

            try:
                url = plugin_conf_p.get(self.plugin_version, 'url')
                size = plugin_conf_p.getint(self.plugin_version, 'size')
                checksum = plugin_conf_p.get(self.plugin_version, 'checksum')
                timestamp = plugin_conf_p.getfloat(self.plugin_version, 'timestamp')
                ok = True
            except KeyError:
                log.error("Error reading plugin.conf")
            
        finally:
            os.close(local_conf_fp)
            os.remove(local_conf)

        return url, size, checksum, timestamp, ok
        

    def create_plugin_dir(self):
        if not os.path.exists(self.plugin_path):
            try:
                log.debug("Creating plugin directory: %s" % self.plugin_path)
                os.umask(0)
                os.makedirs(self.plugin_path, 0755)
                return True
            except (OSError, IOError), e:
                log.error("Unable to create directory: %s" % e.strerror)
                return False

        return True


    def download_plugin(self, url, size, checksum, timestamp, callback=None):
        log.debug("Downloading %s plug-in from %s to %s" % (self.plugin_version, url, self.plugin_path))

        if not self.create_plugin_dir():
            return False, "Failed to create plug-in directory: %s" % self.plugin_path

        plugin_file = os.path.join(self.plugin_path, self.plugin_name)
        
        try:
            filename, headers = urllib.urlretrieve(url, plugin_file, callback)
        except IOError, e:
            log.error("Plug-in download failed: %s" % e.strerror)
            return False, e.strerror
        
        calc_checksum = sha.new(file(plugin_file, 'r').read()).hexdigest()
        log.debug("D/L file checksum=%s" % calc_checksum)

        return True, plugin_file


    def check_for_plugin(self):
        return os.path.exists(os.path.join(self.plugin_path, self.plugin_name)) and \
            utils.to_bool(sys_cfg.hplip.plugin)

    
    def run_plugin(self, mode=GUI_MODE, callback=None):
        plugin_file = os.path.join(self.plugin_path, self.plugin_name)
        
        if not os.path.exists(plugin_file):
            return False
        
        if mode == GUI_MODE:
            return os.system("sh %s -- -u" % plugin_file) == 0
        else:
            return os.system("sh %s -- -i" % plugin_file) == 0
    
        
       
        
