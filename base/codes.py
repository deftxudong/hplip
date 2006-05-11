# -*- coding: utf-8 -*-
#
# (c) Copyright 2003-2006 Hewlett-Packard Development Company, L.P.
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
#
# NOTE: This module is safe for 'from codes import *'
#

# Messaging Error Codes (result-code=)

ERROR_SUCCESS = 0
ERROR_UNKNOWN_ERROR = 1
ERROR_DEVICE_NOT_FOUND = 2
ERROR_INVALID_DEVICE_ID = 3
ERROR_INVALID_DEVICE_URI = 4
ERROR_INVALID_MSG_TYPE = 5
ERROR_INVALID_DATA_ENCODING = 6
ERROR_INVALID_CHAR_ENCODING = 7
ERROR_DATA_LENGTH_EXCEEDS_MAX = 8
ERROR_DATA_LENGTH_MISMATCH = 9
ERROR_DATA_DIGEST_MISMATCH = 10
ERROR_INVALID_JOB_ID = 11
ERROR_DEVICE_IO_ERROR = 12
ERROR_STRING_QUERY_FAILED = 14
ERROR_QUERY_FAILED = 15
ERROR_GUI_NOT_AVAILABLE = 16
ERROR_NO_CUPS_DEVICES_FOUND = 17 # deprecated
ERROR_NO_PROBED_DEVICES_FOUND = 18
ERROR_INVALID_BUS_TYPE = 19 # operation not supported on bus
ERROR_BUS_TYPE_CANNOT_BE_PROBED = 20
ERROR_DEVICE_BUSY = 21
ERROR_NO_DATA_AVAILABLE = 22
ERROR_INVALID_DEVICEID = 23
ERROR_INVALID_CUPS_VERSION = 24
ERROR_CUPS_NOT_RUNNING = 25
ERROR_DEVICE_STATUS_NOT_AVAILABLE = 26
ERROR_DATA_IN_SHORT_READ = 27
ERROR_INVALID_SERVICE_NAME = 28
ERROR_INVALID_USER_ERROR_CODE = 29
ERROR_ERROR_INVALID_CHANNEL_ID = 30
ERROR_CHANNEL_BUSY = 31
ERROR_CHANNEL_CLOSE_FAILED = 32
ERROR_UNSUPPORTED_BUS_TYPE = 33 # bus not supported
ERROR_DEVICE_DOES_NOT_SUPPORT_OPERATION = 34
ERROR_INVALID_GUI_NAME = 35
ERROR_INTERFACE_BUSY = 36
ERROR_DEVICEOPEN_FAILED_ONE_DEVICE_ONLY = 37
ERROR_DEVICEOPEN_FAILED_DEV_NODE_MOVED = 38
ERROR_TEST_EMAIL_FAILED = 39
#ERROR_SMTP_CONNECT_ERROR = 40
#ERROR_SMTP_RECIPIENTS_REFUSED = 41
#ERROR_SMTP_HELO_ERROR = 42
#ERROR_SMTP_SENDER_REFUSED = 43
#ERROR_SMTP_DATA_ERROR = 44
ERROR_INVALID_HOSTNAME = 45
ERROR_INVALID_PORT_NUMBER = 46
ERROR_NO_CUPS_QUEUE_FOUND_FOR_DEVICE = 47
ERROR_UNSUPPORTED_MODEL = 48
ERROR_FAX_FILE_NOT_FOUND = 49
ERROR_FAX_INCOMPATIBLE_OPTIONS = 50
ERROR_FAX_INVALID_FAX_FILE = 51
ERROR_FAX_MUST_RUN_SENDFAX_FIRST = 52
# --> add new codes here <--
ERROR_UNABLE_TO_BIND_SOCKET = 95
ERROR_UNABLE_TO_CONTACT_SERVICE = 96
ERROR_DEVICE_NOT_OPEN = 98
ERROR_INTERNAL = 99
# If you add new codes, also add the appropriate description
# to g.py for exception description strings.
# Thank you, The Management






# Event and status codes
# These are used for the 'status-code' returned by DeviceQuery (STATUS_*)
# and by the event-code used by Event (EVENT_* + STATUS_*)

# If you add a new EVENT/STATUS code, please add the appropriate
# entry into the STATUS_TO_ERROR_STATE_MAP

STATUS_UNKNOWN = 0

EVENT_START_PRINT_JOB = 500 # sent by hp: backend
EVENT_END_PRINT_JOB = 501 # sent by hp: backend

STATUS_PRINTER_BASE = 1000
STATUS_PRINTER_IDLE = 1000
STATUS_PRINTER_BUSY = 1001
STATUS_PRINTER_PRINTING = 1002
STATUS_PRINTER_TURNING_OFF = 1003
STATUS_PRINTER_REPORT_PRINTING = 1004
STATUS_PRINTER_CANCELING = 1005
STATUS_PRINTER_IO_STALL = 1006
STATUS_PRINTER_DRY_WAIT_TIME = 1007
STATUS_PRINTER_PEN_CHANGE = 1008
STATUS_PRINTER_OUT_OF_PAPER = 1009
STATUS_PRINTER_BANNER_EJECT = 1010
STATUS_PRINTER_BANNER_MISMATCH = 1011
STATUS_PRINTER_PHOTO_MISMATCH = 1012
STATUS_PRINTER_DUPLEX_MISMATCH = 1013
STATUS_PRINTER_MEDIA_JAM = 1014
STATUS_PRINTER_CARRIAGE_STALL = 1015
STATUS_PRINTER_PAPER_STALL = 1016
STATUS_PRINTER_PEN_FAILURE = 1017
STATUS_PRINTER_HARD_ERROR = 1018
STATUS_PRINTER_POWER_DOWN = 1019
STATUS_PRINTER_FRONT_PANEL_TEST = 1020
STATUS_PRINTER_CLEAN_OUT_TRAY_MISSING = 1021
STATUS_PRINTER_OUTPUT_BIN_FULL = 1022
STATUS_PRINTER_MEDIA_SIZE_MISMATCH = 1023
STATUS_PRINTER_MANUAL_DUPLEX_BLOCK = 1024
STATUS_PRINTER_SERVCE_STALL = 1025
STATUS_PRINTER_OUT_OF_INK = 1026 # Also used for out of toner
STATUS_PRINTER_LIO_ERROR = 1027
STATUS_PRINTER_PUMP_STALL = 1028
STATUS_PRINTER_TRAY_2_MISSING = 1029
STATUS_PRINTER_DUPLEXER_MISSING = 1030
STATUS_PRINTER_REAR_TRAY_MISSING = 1031
STATUS_PRINTER_PEN_NOT_LATCHED = 1032
STATUS_PRINTER_BATTERY_VERY_LOW = 1033
STATUS_PRINTER_SPITTOON_FULL = 1034
STATUS_PRINTER_OUTPUT_TRAY_CLOSED = 1035
STATUS_PRINTER_MANUAL_FEED_BLOCKED = 1036
STATUS_PRINTER_REAR_FEED_BLOCKED = 1037
STATUS_PRINTER_TRAY_2_OUT_OF_PAPER = 1038
STATUS_PRINTER_UNABLE_TO_LOAD_FROM_LOCKED_TRAY = 1039
STATUS_PRINTER_NON_HP_INK = 1040
STATUS_PRINTER_PEN_CALIBRATION_RESUME = 1041
STATUS_PRINTER_MEDIA_TYPE_MISMATCH = 1042
STATUS_PRINTER_CUSTOM_MEDIA_MISMATCH = 1043
STATUS_PRINTER_PEN_CLEANING = 1044
STATUS_PRINTER_PEN_CHECKING = 1045

# "synthetic" codes
# set to AGENT_TYPE + base (base: 1500=ink, 1600=laser )
STATUS_PRINTER_LOW_INK_BASE = 1500
STATUS_PRINTER_LOW_BLACK_INK = 1501
STATUS_PRINTER_LOW_TRI_COLOR_INK = 1502
STATUS_PRINTER_LOW_PHOTO_INK = 1503
STATUS_PRINTER_LOW_CYAN_INK = 1504
STATUS_PRINTER_LOW_MAGENTA_INK = 1505
STATUS_PRINTER_LOW_YELLOW_INK = 1506
STATUS_PRINTER_LOW_PHOTO_CYAN_INK = 1507
STATUS_PRINTER_LOW_PHOTO_MAGENTA_INK = 1508
STATUS_PRINTER_LOW_PHOTO_YELLOW_INK = 1509
STATUS_PRINTER_LOW_PHOTO_GRAY_INK = 1510
STATUS_PRINTER_LOW_PHOTO_BLUE_INK = 1511

STATUS_PRINTER_LOW_TONER_BASE = 1600
STATUS_PRINTER_LOW_BLACK_TONER = 1601
STATUS_PRINTER_LOW_CYAN_TONER = 1604
STATUS_PRINTER_LOW_MAGENTA_TONER = 1605
STATUS_PRINTER_LOW_YELLOW_TONER = 1606
# end

# "synthetic" laserjet codes
STATUS_PRINTER_WARMING_UP = 1800
STATUS_PRINTER_LOW_PAPER = 1801
STATUS_PRINTER_DOOR_OPEN = 1802
STATUS_PRINTER_OFFLINE = 1803
STATUS_PRINTER_LOW_TONER = 1804
STATUS_PRINTER_NO_TONER = 1805
STATUS_PRINTER_SERVICE_REQUEST = 1806
STATUS_PRINTER_FUSER_ERROR = 1807
#end

# other "synthetic" codes
STATUS_DEVICE_UNSUPPORTED = 1900
#end

# scan
EVENT_START_SCAN_JOB = 2000
EVENT_END_SCAN_JOB = 2001
EVENT_SCANNER_FAIL = 2002
#end

# fax
EVENT_START_FAX_JOB = 3000
EVENT_END_FAX_JOB = 3001
EVENT_FAX_JOB_FAIL = 3002
EVENT_FAX_JOB_CANCELED = 3003
STATUS_FAX_TX_ACTIVE = 3004
STATUS_FAX_RX_ACTIVE = 3005
#end

# copy
EVENT_START_COPY_JOB = 4000
EVENT_END_COPY_JOB = 4001
EVENT_COPY_JOB_FAIL = 4002
#end

# Adding the ERROR_CODE_BASE to the above
# ERROR codes will produce a event/status code
# e.g., ERROR_DATA_IN_SHORT_READ=27 -> 5027 status/event code
ERROR_CODE_BASE = 5000
EVENT_ERROR_SUCCESS = 5000
EVENT_ERROR_UNKNOWN_ERROR = 5001
EVENT_ERROR_DEVICE_NOT_FOUND = 5002
EVENT_ERROR_INVALID_DEVICE_ID = 5003
EVENT_ERROR_INVALID_DEVICE_URI = 5004
EVENT_ERROR_INVALID_MSG_TYPE = 5005
EVENT_ERROR_INVALID_DATA_ENCODING = 5006
EVENT_ERROR_INVALID_CHAR_ENCODING = 5007
EVENT_ERROR_DATA_LENGTH_EXCEEDS_MAX = 5008
EVENT_ERROR_DATA_LENGTH_MISMATCH = 5009
EVENT_ERROR_DATA_DIGEST_MISMATCH = 5010
EVENT_ERROR_INVALID_JOB_ID = 5011
EVENT_ERROR_DEVICE_IO_ERROR = 5012
EVENT_ERROR_STRING_QUERY_FAILED = 5014
EVENT_ERROR_QUERY_FAILED = 5015
EVENT_ERROR_GUI_NOT_AVAILABLE = 5016
EVENT_ERROR_NO_CUPS_DEVICES_FOUND = 5017 # deprecated
EVENT_ERROR_NO_PROBED_DEVICES_FOUND = 5018
EVENT_ERROR_INVALID_BUS_TYPE = 5019 # operation not supported on bus
EVENT_ERROR_BUS_TYPE_CANNOT_BE_PROBED = 5020
EVENT_ERROR_DEVICE_BUSY = 5021
EVENT_ERROR_NO_DATA_AVAILABLE = 5022
EVENT_ERROR_INVALID_DEVICEID = 5023
EVENT_ERROR_INVALID_CUPS_VERSION = 5024
EVENT_ERROR_CUPS_NOT_RUNNING = 5025
EVENT_ERROR_DEVICE_STATUS_NOT_AVAILABLE = 5026
EVENT_ERROR_DATA_IN_SHORT_READ = 5027
EVENT_ERROR_INVALID_SERVICE_NAME = 5028
EVENT_ERROR_INVALID_USER_ERROR_CODE = 5029
EVENT_ERROR_ERROR_INVALID_CHANNEL_ID = 5030
EVENT_ERROR_CHANNEL_BUSY = 5031
EVENT_ERROR_CHANNEL_CLOSE_FAILED = 5032
EVENT_ERROR_UNSUPPORTED_BUS_TYPE = 5033 # bus not supported
EVENT_ERROR_DEVICE_DOES_NOT_SUPPORT_OPERATION = 5034
EVENT_ERROR_INVALID_GUI_NAME = 5035
EVENT_ERROR_INTERFACE_BUSY = 5036
EVENT_ERROR_DEVICEOPEN_FAILED_ONE_DEVICE_ONLY = 5037
EVENT_ERROR_DEVICEOPEN_FAILED_DEV_NODE_MOVED = 5038
EVENT_ERROR_FAX_MUST_RUN_SENDFAX_FIRST = 5052
# end

# pcard
EVENT_START_PCARD_JOB = 6000
EVENT_END_PCARD_JOB = 6001
EVENT_PCARD_JOB_FAIL = 6002
EVENT_PCARD_UNABLE_TO_MOUNT = 6003
EVENT_PCARD_FILES_TRANSFERED = 6004
# end

EVENT_MAX_USER_EVENT = 7999
# end of user events
# start of internal events

# fax (internal events)
EVENT_FAX_MIN = 8000
EVENT_FAX_RENDER_COMPLETE = 8000 # sent by hpssd to hp-sendfax after job rendered
EVENT_FAX_ADDRESS_BOOK_UPDATED = 8002 # Sent by FAB to indicate that the dB has changed
EVENT_FAX_RENDER_DISTANT_EARLY_WARNING = 8003
EVENT_FAX_MAX = 8999
# end

# end of events


# Error states
ERROR_STATE_CLEAR = 0        # Show icon w/o overlay
ERROR_STATE_OK = 1           # Icon w/ "OK" overlay
ERROR_STATE_WARNING = 2      # Icon w/ triangle "!" overlay
ERROR_STATE_ERROR = 3        # Icon w/ circle "X" overlay
ERROR_STATE_LOW_SUPPLIES = 4 # Icon w/ supplies overlay
ERROR_STATE_BUSY = 5         # Icon with busy overlay
ERROR_STATE_LOW_PAPER = 6    # Icon w/ paper low overlay
#end


# Map of status/event codes to UI states
STATUS_TO_ERROR_STATE_MAP = {
    STATUS_UNKNOWN : ERROR_STATE_CLEAR,
    EVENT_START_PRINT_JOB : ERROR_STATE_BUSY,
    EVENT_END_PRINT_JOB   : ERROR_STATE_OK,
    STATUS_PRINTER_IDLE : ERROR_STATE_CLEAR,
    STATUS_PRINTER_BUSY : ERROR_STATE_BUSY,
    STATUS_PRINTER_PRINTING : ERROR_STATE_BUSY,
    STATUS_PRINTER_TURNING_OFF : ERROR_STATE_BUSY,
    STATUS_PRINTER_REPORT_PRINTING : ERROR_STATE_BUSY,
    STATUS_PRINTER_CANCELING : ERROR_STATE_BUSY,
    STATUS_PRINTER_IO_STALL : ERROR_STATE_ERROR,
    STATUS_PRINTER_DRY_WAIT_TIME : ERROR_STATE_BUSY,
    STATUS_PRINTER_PEN_CHANGE : ERROR_STATE_WARNING,
    STATUS_PRINTER_OUT_OF_PAPER : ERROR_STATE_ERROR,
    STATUS_PRINTER_BANNER_EJECT : ERROR_STATE_ERROR,
    STATUS_PRINTER_BANNER_MISMATCH : ERROR_STATE_WARNING,
    STATUS_PRINTER_PHOTO_MISMATCH : ERROR_STATE_WARNING,
    STATUS_PRINTER_DUPLEX_MISMATCH : ERROR_STATE_WARNING,
    STATUS_PRINTER_MEDIA_JAM : ERROR_STATE_ERROR,
    STATUS_PRINTER_CARRIAGE_STALL : ERROR_STATE_ERROR,
    STATUS_PRINTER_PAPER_STALL : ERROR_STATE_ERROR,
    STATUS_PRINTER_PEN_FAILURE : ERROR_STATE_ERROR,
    STATUS_PRINTER_HARD_ERROR : ERROR_STATE_ERROR,
    STATUS_PRINTER_POWER_DOWN : ERROR_STATE_ERROR,
    STATUS_PRINTER_FRONT_PANEL_TEST : ERROR_STATE_ERROR,
    STATUS_PRINTER_CLEAN_OUT_TRAY_MISSING : ERROR_STATE_ERROR,
    STATUS_PRINTER_OUTPUT_BIN_FULL : ERROR_STATE_ERROR,
    STATUS_PRINTER_MEDIA_SIZE_MISMATCH : ERROR_STATE_WARNING,
    STATUS_PRINTER_MANUAL_DUPLEX_BLOCK : ERROR_STATE_ERROR,
    STATUS_PRINTER_SERVCE_STALL : ERROR_STATE_ERROR,
    STATUS_PRINTER_OUT_OF_INK : ERROR_STATE_ERROR,
    STATUS_PRINTER_LIO_ERROR : ERROR_STATE_ERROR,
    STATUS_PRINTER_PUMP_STALL : ERROR_STATE_ERROR,
    STATUS_PRINTER_TRAY_2_MISSING : ERROR_STATE_ERROR,
    STATUS_PRINTER_DUPLEXER_MISSING : ERROR_STATE_ERROR,
    STATUS_PRINTER_REAR_TRAY_MISSING : ERROR_STATE_ERROR,
    STATUS_PRINTER_PEN_NOT_LATCHED : ERROR_STATE_ERROR,
    STATUS_PRINTER_BATTERY_VERY_LOW : ERROR_STATE_WARNING,
    STATUS_PRINTER_SPITTOON_FULL : ERROR_STATE_ERROR,
    STATUS_PRINTER_OUTPUT_TRAY_CLOSED : ERROR_STATE_ERROR,
    STATUS_PRINTER_MANUAL_FEED_BLOCKED : ERROR_STATE_ERROR,
    STATUS_PRINTER_REAR_FEED_BLOCKED : ERROR_STATE_ERROR,
    STATUS_PRINTER_TRAY_2_OUT_OF_PAPER : ERROR_STATE_LOW_PAPER,
    STATUS_PRINTER_UNABLE_TO_LOAD_FROM_LOCKED_TRAY : ERROR_STATE_ERROR,
    STATUS_PRINTER_NON_HP_INK : ERROR_STATE_WARNING,
    STATUS_PRINTER_PEN_CALIBRATION_RESUME : ERROR_STATE_WARNING,
    STATUS_PRINTER_MEDIA_TYPE_MISMATCH : ERROR_STATE_WARNING,
    STATUS_PRINTER_CUSTOM_MEDIA_MISMATCH : ERROR_STATE_WARNING,
    STATUS_PRINTER_PEN_CLEANING : ERROR_STATE_WARNING,
    STATUS_PRINTER_PEN_CLEANING : ERROR_STATE_WARNING,
    STATUS_PRINTER_WARMING_UP : ERROR_STATE_BUSY,
    STATUS_PRINTER_LOW_PAPER : ERROR_STATE_LOW_PAPER,
    STATUS_PRINTER_DOOR_OPEN : ERROR_STATE_ERROR,
    STATUS_PRINTER_OFFLINE : ERROR_STATE_ERROR,
    STATUS_PRINTER_LOW_TONER : ERROR_STATE_LOW_SUPPLIES,
    STATUS_PRINTER_NO_TONER : ERROR_STATE_LOW_SUPPLIES,
    STATUS_PRINTER_SERVICE_REQUEST : ERROR_STATE_ERROR,
    STATUS_PRINTER_FUSER_ERROR : ERROR_STATE_ERROR,
    STATUS_DEVICE_UNSUPPORTED : ERROR_STATE_ERROR,
    # The following block are EVENTs because they are only
    # recieved as events from hpiod, hp backend, etc.
    # i.e., a device does not produce status codes in this range
    EVENT_ERROR_SUCCESS : ERROR_STATE_CLEAR,
    EVENT_ERROR_UNKNOWN_ERROR : ERROR_STATE_ERROR,
    EVENT_ERROR_DEVICE_NOT_FOUND : ERROR_STATE_ERROR,
    EVENT_ERROR_INVALID_DEVICE_ID : ERROR_STATE_ERROR,
    EVENT_ERROR_INVALID_DEVICE_URI : ERROR_STATE_ERROR,
    EVENT_ERROR_INVALID_MSG_TYPE : ERROR_STATE_ERROR,
    EVENT_ERROR_INVALID_DATA_ENCODING : ERROR_STATE_ERROR,
    EVENT_ERROR_INVALID_CHAR_ENCODING : ERROR_STATE_ERROR,
    EVENT_ERROR_DATA_LENGTH_EXCEEDS_MAX : ERROR_STATE_WARNING,
    EVENT_ERROR_DATA_LENGTH_MISMATCH : ERROR_STATE_ERROR,
    EVENT_ERROR_DATA_DIGEST_MISMATCH : ERROR_STATE_ERROR,
    EVENT_ERROR_INVALID_JOB_ID : ERROR_STATE_ERROR,
    EVENT_ERROR_DEVICE_IO_ERROR : ERROR_STATE_ERROR,
    EVENT_ERROR_STRING_QUERY_FAILED : ERROR_STATE_ERROR,
    EVENT_ERROR_QUERY_FAILED : ERROR_STATE_ERROR,
    EVENT_ERROR_GUI_NOT_AVAILABLE : ERROR_STATE_WARNING,
    EVENT_ERROR_NO_CUPS_DEVICES_FOUND : ERROR_STATE_WARNING,
    EVENT_ERROR_NO_PROBED_DEVICES_FOUND : ERROR_STATE_WARNING,
    EVENT_ERROR_INVALID_BUS_TYPE : ERROR_STATE_ERROR,
    EVENT_ERROR_BUS_TYPE_CANNOT_BE_PROBED : ERROR_STATE_ERROR,
    EVENT_ERROR_DEVICE_BUSY : ERROR_STATE_BUSY,
    EVENT_ERROR_NO_DATA_AVAILABLE : ERROR_STATE_ERROR,
    EVENT_ERROR_INVALID_DEVICEID : ERROR_STATE_ERROR,
    EVENT_ERROR_INVALID_CUPS_VERSION : ERROR_STATE_ERROR,
    EVENT_ERROR_CUPS_NOT_RUNNING : ERROR_STATE_ERROR,
    EVENT_ERROR_DEVICE_STATUS_NOT_AVAILABLE : ERROR_STATE_ERROR,
    EVENT_ERROR_DATA_IN_SHORT_READ : ERROR_STATE_ERROR,
    EVENT_ERROR_INVALID_SERVICE_NAME : ERROR_STATE_ERROR,
    EVENT_ERROR_INVALID_USER_ERROR_CODE : ERROR_STATE_ERROR,
    EVENT_ERROR_ERROR_INVALID_CHANNEL_ID : ERROR_STATE_ERROR,
    EVENT_ERROR_CHANNEL_BUSY : ERROR_STATE_BUSY,
    EVENT_ERROR_CHANNEL_CLOSE_FAILED : ERROR_STATE_ERROR,
    EVENT_ERROR_UNSUPPORTED_BUS_TYPE : ERROR_STATE_ERROR,
    EVENT_ERROR_DEVICE_DOES_NOT_SUPPORT_OPERATION : ERROR_STATE_ERROR,
    EVENT_ERROR_INVALID_GUI_NAME : ERROR_STATE_ERROR,
    EVENT_ERROR_INTERFACE_BUSY : ERROR_STATE_BUSY,
    EVENT_ERROR_DEVICEOPEN_FAILED_ONE_DEVICE_ONLY : ERROR_STATE_ERROR,
    EVENT_ERROR_DEVICEOPEN_FAILED_DEV_NODE_MOVED : ERROR_STATE_ERROR,
    
    EVENT_START_SCAN_JOB : ERROR_STATE_BUSY,
    EVENT_END_SCAN_JOB : ERROR_STATE_OK,
    EVENT_SCANNER_FAIL : ERROR_STATE_ERROR,
    
    EVENT_START_FAX_JOB : ERROR_STATE_BUSY,
    EVENT_END_FAX_JOB : ERROR_STATE_OK,
    EVENT_FAX_JOB_FAIL : ERROR_STATE_ERROR,
    EVENT_FAX_JOB_CANCELED : ERROR_STATE_ERROR,
    STATUS_FAX_TX_ACTIVE : ERROR_STATE_BUSY,
    STATUS_FAX_RX_ACTIVE : ERROR_STATE_BUSY,
    
    EVENT_START_COPY_JOB : ERROR_STATE_BUSY,
    EVENT_END_COPY_JOB : ERROR_STATE_OK,
    
    EVENT_START_PCARD_JOB : ERROR_STATE_BUSY,
    EVENT_END_PCARD_JOB : ERROR_STATE_CLEAR,
    
    EVENT_PCARD_JOB_FAIL : ERROR_STATE_ERROR,
    EVENT_PCARD_UNABLE_TO_MOUNT : ERROR_STATE_ERROR,
    EVENT_PCARD_FILES_TRANSFERED : ERROR_STATE_OK,
}


# Device states
DEVICE_STATE_NOT_FOUND = -1
DEVICE_STATE_FOUND = 0
DEVICE_STATE_JUST_FOUND = 1


# I/O states
IO_STATE_HP_OPEN = 0
IO_STATE_HP_READY = 1
IO_STATE_HP_NOT_AVAIL = 2
IO_STATE_NON_HP = 3

#
# Defines for model query types and status query
#

# agent info

# 'kind'
AGENT_KIND_NONE = 0
AGENT_KIND_HEAD = 1 # InkJet head (no ink)
AGENT_KIND_SUPPLY = 2 # InkJet supply (ink tank)
AGENT_KIND_HEAD_AND_SUPPLY = 3 # InkJet (cartridge)
AGENT_KIND_TONER_CARTRIDGE = 4 # LaserJet
AGENT_KIND_MAINT_KIT = 5 # LaserJet "Maintenance kit (fuser)"
AGENT_KIND_ADF_KIT = 6 # LaserJet "Document feeder kit"
AGENT_KIND_DRUM_KIT = 7 # LaserJet
AGENT_KIND_TRANSFER_KIT = 8 # LaserJet
AGENT_KIND_INT_BATTERY = 9 # Mobile deskjet (DJ450, etc)
AGENT_KIND_UNKNOWN = 0x3e # (62)

# 'type'
AGENT_TYPE_NONE = 0
AGENT_TYPE_BLACK = 1
AGENT_TYPE_CMY = 2
AGENT_TYPE_KCM = 3
AGENT_TYPE_CYAN = 4
AGENT_TYPE_MAGENTA = 5
AGENT_TYPE_YELLOW = 6
AGENT_TYPE_CYAN_LOW = 7
AGENT_TYPE_MAGENTA_LOW = 8
AGENT_TYPE_YELLOW_LOW = 9
AGENT_TYPE_GGK = 10 # 2 shades of grey and black
AGENT_TYPE_BLUE = 11
AGENT_TYPE_KCMY_CM = 12 
AGENT_TYPE_LC_LM = 13 # light cyan and light magenta
AGENT_TYPE_Y_M = 14 # yellow and magenta
AGENT_TYPE_C_K = 15 # cyan and black
AGENT_TYPE_LG_PK = 16 # light grey and photo black
AGENT_TYPE_LG = 17 # light grey
AGENT_TYPE_G = 18 # medium grey
AGENT_TYPE_PG = 19 # photo grey
AGENT_TYPE_WHITE = 0x20 # For ISO 10180 compatibility
AGENT_TYPE_RED = 0x21 # For ISO 10180 compatibility
AGENT_TYPE_UNSPECIFIED = 0x3e # (62) Used for kind = 5, 6, 7, 8, or 9
AGENT_TYPE_ERROR = 0x3f # (63)

# 'health'
AGENT_HEALTH_OK = 0
AGENT_HEALTH_MISINSTALLED = 1 # supply/cart
AGENT_HEALTH_FAIR_MODERATE = 1 # head
AGENT_HEALTH_INCORRECT = 2
AGENT_HEALTH_FAILED = 3
AGENT_HEALTH_OVERTEMP = 4 # Battery
AGENT_HEALTH_CHARGING = 5 # Battery
AGENT_HEALTH_DISCHARGING = 6 # Battery
AGENT_HEALTH_UNKNOWN = 0xff

# 'level'
AGENT_LEVEL_TRIGGER_SUFFICIENT_0 = 0
AGENT_LEVEL_TRIGGER_SUFFICIENT_1 = 1
AGENT_LEVEL_TRIGGER_SUFFICIENT_2 = 2
AGENT_LEVEL_TRIGGER_SUFFICIENT_3 = 3
AGENT_LEVEL_TRIGGER_SUFFICIENT_4 = 4
AGENT_LEVEL_TRIGGER_MAY_BE_LOW = 5
AGENT_LEVEL_TRIGGER_PROBABLY_OUT = 6
AGENT_LEVEL_TRIGGER_ALMOST_DEFINITELY_OUT = 7

# "Computed" configurations
AGENT_CONFIG_NONE = 0
AGENT_CONFIG_BLACK_ONLY = 1
AGENT_CONFIG_PHOTO_ONLY = 2
AGENT_CONFIG_COLOR_ONLY = 3
AGENT_CONFIG_GREY_ONLY = 4
AGENT_CONFIG_COLOR_AND_BLACK = 5
AGENT_CONFIG_COLOR_AND_PHOTO = 6
AGENT_CONFIG_COLOR_AND_GREY = 7
AGENT_CONFIG_INVALID = 99

# align-types
ALIGN_TYPE_NONE = 0
ALIGN_TYPE_AUTO = 1
ALIGN_TYPE_8XX = 2
ALIGN_TYPE_9XX = 3
ALIGN_TYPE_LIDIL_0_3_8 = 4
ALIGN_TYPE_LIDIL_0_4_3 = 5
ALIGN_TYPE_LIDIL_AIO = 6
ALIGN_TYPE_LIDIL_VIP = 7
ALIGN_TYPE_DESKJET_450 = 8
ALIGN_TYPE_9XX_NO_EDGE_ALIGN = 9
ALIGN_TYPE_LBOW = 10

# clean-types
CLEAN_TYPE_NONE = 0
CLEAN_TYPE_PCL = 1
CLEAN_TYPE_LIDIL = 2
CLEAN_TYPE_PCL_WITH_PRINTOUT = 3

# color-cal-types
COLOR_CAL_TYPE_NONE = 0
COLOR_CAL_TYPE_DESKJET_450 = 1
COLOR_CAL_TYPE_MALIBU_CRICK = 2
COLOR_CAL_TYPE_STRINGRAY_LONGBOW_TORNADO = 3
COLOR_CAL_TYPE_CONNERY = 4
COLOR_CAL_TYPE_COUSTEAU = 5

# status-types
STATUS_TYPE_NONE = 0
STATUS_TYPE_VSTATUS = 1
STATUS_TYPE_S = 2
STATUS_TYPE_LJ = 3
STATUS_TYPE_S_W_BATTERY = 4
STATUS_TYPE_S_SNMP = 5
STATUS_TYPE_LJ_XML = 6

# tech-types
TECH_TYPE_NONE = 0
TECH_TYPE_MONO_INK = 1
TECH_TYPE_COLOR_INK = 2
TECH_TYPE_MONO_LASER = 3
TECH_TYPE_COLOR_LASER = 4

# support-type
SUPPORT_TYPE_NONE = 0
SUPPORT_TYPE_HPIJS = 1
SUPPORT_TYPE_HPLIP = 2

# fax-types
FAX_TYPE_NONE = 0
FAX_TYPE_BLACK_SEND_EARLY_OPEN = 1 # newer models
FAX_TYPE_BLACK_SEND_LATE_OPEN = 2 # older models
FAX_TYPE_BLACK_AND_COLOR_SEND = 3 # future

# pcard-types
PCARD_TYPE_NONE = 0
PCARD_TYPE_MLC = 1
PCARD_TYPE_USB_MASS_STORAGE = 2

# scan-types
SCAN_TYPE_NONE = 0
SCAN_TYPE_SCL = 1
SCAN_TYPE_PML = 2

# copy-types
COPY_TYPE_NONE = 0
COPY_TYPE_DEVICE = 1
COPY_TYPE_SCAN_TO_PRINT = 2

# 'top_door' (lid)
TOP_DOOR_NOT_PRESENT = 0
TOP_DOOR_CLOSED = 1
TOP_DOOR_OPEN = 2

# 'supply_door'
SUPPLY_DOOR_NOT_PRESENT = 0
SUPPLY_DOOR_CLOSED = 1
SUPPLY_DOOR_OPEN = 2

# 'media_path'
MEDIA_PATH_NOT_PRESENT = 0 # S:00 means banner not present
MEDIA_PATH_CUT_SHEET = 1 # S:01 means banner present/engaged
MEDIA_PATH_BANNER = 2
MEDIA_PATH_PHOTO = 3

# 'photo_tray'(S:03 photo/hagaki)
PHOTO_TRAY_NOT_PRESENT = 0
PHOTO_TRAY_NOT_ENGAGED = 1
PHOTO_TRAY_ENGAGED = 2

# 'duplexer' (S:02 cleanout)
DUPLEXER_NOT_PRESENT = 0
DUPLEXER_DOOR_CLOSED = 1
DUPLEXER_DOOR_OPEN = 2

# 'in_tray1' & 'in_tray2'
IN_TRAY_NOT_PRESENT = 0
IN_TRAY_PRESENT = 1 # for !S:02, test for > IN_TRAY_NOT_PRESENT
IN_TRAY_DEFAULT = 2 # S:02 only
IN_TRAY_LOCKED = 3 # S:02 only

# 'io-support'
IO_SUPPORT_PARALLEL = 0x1
IO_SUPPORT_USB = 0x2
IO_SUPPORT_NETWORK = 0x4
IO_SUPPORT_WIRELESS = 0x8
IO_SUPPORT_BLUETOOTH = 0x10

# Model categories
MODEL_TYPE_UNSUPPORTED = -1
MODEL_TYPE_COLOR_INKJET = 0
MODEL_TYPE_PHOTOSMART = 1
MODEL_TYPE_COLOR_LASER = 2
MODEL_TYPE_COLOR_LASER_AIO = 3
MODEL_TYPE_COLOR_INKJET_AIO = 4
MODEL_TYPE_MONO_LASER = 5
MODEL_TYPE_MONO_LASER_AIO = 6

# 'io-mode'
IO_MODE_UNI = 0
IO_MODE_RAW = 1
IO_MODE_MLC = 2
IO_MODE_DOT4 = 3
