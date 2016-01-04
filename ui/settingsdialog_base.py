# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingsdialog_base.ui'
#
# Created: Thu Jun 15 14:00:36 2006
#      by: The PyQt User Interface Compiler (pyuic) 3.15.1
#
# WARNING! All changes made in this file will be lost!


from qt import *


class SettingsDialog_base(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("SettingsDialog_base")


        SettingsDialog_baseLayout = QGridLayout(self,1,1,11,6,"SettingsDialog_baseLayout")

        self.pushButton30 = QPushButton(self,"pushButton30")

        SettingsDialog_baseLayout.addWidget(self.pushButton30,1,2)

        self.pushButton31 = QPushButton(self,"pushButton31")

        SettingsDialog_baseLayout.addWidget(self.pushButton31,1,1)
        spacer40 = QSpacerItem(430,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        SettingsDialog_baseLayout.addItem(spacer40,1,0)

        self.TabWidget = QTabWidget(self,"TabWidget")

        self.CleaningLevels = QWidget(self.TabWidget,"CleaningLevels")
        CleaningLevelsLayout = QGridLayout(self.CleaningLevels,1,1,11,6,"CleaningLevelsLayout")

        self.textLabel3_2_2 = QLabel(self.CleaningLevels,"textLabel3_2_2")

        CleaningLevelsLayout.addWidget(self.textLabel3_2_2,0,0)

        self.line1_2_2 = QFrame(self.CleaningLevels,"line1_2_2")
        self.line1_2_2.setFrameShape(QFrame.HLine)
        self.line1_2_2.setFrameShadow(QFrame.Sunken)
        self.line1_2_2.setFrameShape(QFrame.HLine)

        CleaningLevelsLayout.addWidget(self.line1_2_2,1,0)
        spacer8 = QSpacerItem(20,30,QSizePolicy.Minimum,QSizePolicy.Expanding)
        CleaningLevelsLayout.addItem(spacer8,5,0)

        self.autoRefreshCheckBox = QCheckBox(self.CleaningLevels,"autoRefreshCheckBox")

        CleaningLevelsLayout.addWidget(self.autoRefreshCheckBox,2,0)

        self.CleaningLevel = QButtonGroup(self.CleaningLevels,"CleaningLevel")
        self.CleaningLevel.setColumnLayout(0,Qt.Vertical)
        self.CleaningLevel.layout().setSpacing(6)
        self.CleaningLevel.layout().setMargin(11)
        CleaningLevelLayout = QGridLayout(self.CleaningLevel.layout())
        CleaningLevelLayout.setAlignment(Qt.AlignTop)
        spacer9_2 = QSpacerItem(290,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        CleaningLevelLayout.addItem(spacer9_2,0,2)

        self.textLabel1_4 = QLabel(self.CleaningLevel,"textLabel1_4")

        CleaningLevelLayout.addWidget(self.textLabel1_4,0,0)

        layout7 = QHBoxLayout(None,0,6,"layout7")

        self.AutoRefreshRate = QSpinBox(self.CleaningLevel,"AutoRefreshRate")
        self.AutoRefreshRate.setEnabled(0)
        self.AutoRefreshRate.setWrapping(1)
        self.AutoRefreshRate.setButtonSymbols(QSpinBox.PlusMinus)
        self.AutoRefreshRate.setMaxValue(60)
        self.AutoRefreshRate.setMinValue(1)
        self.AutoRefreshRate.setValue(1)
        layout7.addWidget(self.AutoRefreshRate)

        self.textLabel1_3 = QLabel(self.CleaningLevel,"textLabel1_3")
        layout7.addWidget(self.textLabel1_3)

        CleaningLevelLayout.addLayout(layout7,0,1)

        CleaningLevelsLayout.addWidget(self.CleaningLevel,3,0)

        self.refreshScopeButtonGroup = QButtonGroup(self.CleaningLevels,"refreshScopeButtonGroup")
        self.refreshScopeButtonGroup.setColumnLayout(0,Qt.Vertical)
        self.refreshScopeButtonGroup.layout().setSpacing(6)
        self.refreshScopeButtonGroup.layout().setMargin(11)
        refreshScopeButtonGroupLayout = QGridLayout(self.refreshScopeButtonGroup.layout())
        refreshScopeButtonGroupLayout.setAlignment(Qt.AlignTop)

        self.radioButton1 = QRadioButton(self.refreshScopeButtonGroup,"radioButton1")
        self.radioButton1.setEnabled(0)
        self.radioButton1.setChecked(1)

        refreshScopeButtonGroupLayout.addWidget(self.radioButton1,0,0)

        self.radioButton2 = QRadioButton(self.refreshScopeButtonGroup,"radioButton2")
        self.radioButton2.setEnabled(0)

        refreshScopeButtonGroupLayout.addWidget(self.radioButton2,1,0)

        CleaningLevelsLayout.addWidget(self.refreshScopeButtonGroup,4,0)
        self.TabWidget.insertTab(self.CleaningLevels,QString.fromLatin1(""))

        self.EmailAlerts = QWidget(self.TabWidget,"EmailAlerts")
        EmailAlertsLayout = QGridLayout(self.EmailAlerts,1,1,11,6,"EmailAlertsLayout")

        self.textLabel3_2 = QLabel(self.EmailAlerts,"textLabel3_2")

        EmailAlertsLayout.addMultiCellWidget(self.textLabel3_2,0,0,0,1)

        self.line1_2_2_2 = QFrame(self.EmailAlerts,"line1_2_2_2")
        self.line1_2_2_2.setFrameShape(QFrame.HLine)
        self.line1_2_2_2.setFrameShadow(QFrame.Sunken)
        self.line1_2_2_2.setFrameShape(QFrame.HLine)

        EmailAlertsLayout.addMultiCellWidget(self.line1_2_2_2,1,1,0,1)

        self.EmailCheckBox = QCheckBox(self.EmailAlerts,"EmailCheckBox")

        EmailAlertsLayout.addMultiCellWidget(self.EmailCheckBox,2,2,0,1)

        self.EmailTestButton = QPushButton(self.EmailAlerts,"EmailTestButton")
        self.EmailTestButton.setEnabled(0)

        EmailAlertsLayout.addWidget(self.EmailTestButton,6,0)
        spacer9_3 = QSpacerItem(491,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        EmailAlertsLayout.addItem(spacer9_3,6,1)

        self.groupBox1 = QGroupBox(self.EmailAlerts,"groupBox1")
        self.groupBox1.setColumnLayout(0,Qt.Vertical)
        self.groupBox1.layout().setSpacing(6)
        self.groupBox1.layout().setMargin(11)
        groupBox1Layout = QGridLayout(self.groupBox1.layout())
        groupBox1Layout.setAlignment(Qt.AlignTop)

        layout11 = QHBoxLayout(None,0,6,"layout11")

        self.textLabel20 = QLabel(self.groupBox1,"textLabel20")
        layout11.addWidget(self.textLabel20)

        layout8 = QVBoxLayout(None,0,6,"layout8")

        self.EmailAddress = QLineEdit(self.groupBox1,"EmailAddress")
        self.EmailAddress.setEnabled(0)
        layout8.addWidget(self.EmailAddress)

        self.textLabel1 = QLabel(self.groupBox1,"textLabel1")
        layout8.addWidget(self.textLabel1)
        layout11.addLayout(layout8)

        groupBox1Layout.addLayout(layout11,0,0)

        EmailAlertsLayout.addMultiCellWidget(self.groupBox1,3,3,0,1)

        self.groupBox2 = QGroupBox(self.EmailAlerts,"groupBox2")
        self.groupBox2.setColumnLayout(0,Qt.Vertical)
        self.groupBox2.layout().setSpacing(6)
        self.groupBox2.layout().setMargin(11)
        groupBox2Layout = QGridLayout(self.groupBox2.layout())
        groupBox2Layout.setAlignment(Qt.AlignTop)

        layout12 = QHBoxLayout(None,0,6,"layout12")

        self.textLabel2 = QLabel(self.groupBox2,"textLabel2")
        layout12.addWidget(self.textLabel2)

        layout10 = QVBoxLayout(None,0,6,"layout10")

        self.senderLineEdit = QLineEdit(self.groupBox2,"senderLineEdit")
        self.senderLineEdit.setEnabled(0)
        layout10.addWidget(self.senderLineEdit)

        self.textLabel3 = QLabel(self.groupBox2,"textLabel3")
        layout10.addWidget(self.textLabel3)
        layout12.addLayout(layout10)

        groupBox2Layout.addLayout(layout12,0,0)

        EmailAlertsLayout.addMultiCellWidget(self.groupBox2,4,4,0,1)
        spacer5 = QSpacerItem(20,90,QSizePolicy.Minimum,QSizePolicy.Expanding)
        EmailAlertsLayout.addItem(spacer5,5,1)
        spacer12 = QSpacerItem(20,80,QSizePolicy.Minimum,QSizePolicy.Expanding)
        EmailAlertsLayout.addItem(spacer12,5,0)
        self.TabWidget.insertTab(self.EmailAlerts,QString.fromLatin1(""))

        self.FunctionCommands = QWidget(self.TabWidget,"FunctionCommands")
        FunctionCommandsLayout = QGridLayout(self.FunctionCommands,1,1,11,6,"FunctionCommandsLayout")

        self.line1_2_2_3 = QFrame(self.FunctionCommands,"line1_2_2_3")
        self.line1_2_2_3.setFrameShape(QFrame.HLine)
        self.line1_2_2_3.setFrameShadow(QFrame.Sunken)
        self.line1_2_2_3.setFrameShape(QFrame.HLine)

        FunctionCommandsLayout.addMultiCellWidget(self.line1_2_2_3,1,1,0,1)

        self.textLabel3_2_2_2 = QLabel(self.FunctionCommands,"textLabel3_2_2_2")

        FunctionCommandsLayout.addMultiCellWidget(self.textLabel3_2_2_2,0,0,0,1)

        self.textLabel1_2 = QLabel(self.FunctionCommands,"textLabel1_2")

        FunctionCommandsLayout.addMultiCellWidget(self.textLabel1_2,2,2,0,1)

        layout8_2 = QHBoxLayout(None,0,6,"layout8_2")

        self.PrintCommand = QLineEdit(self.FunctionCommands,"PrintCommand")
        layout8_2.addWidget(self.PrintCommand)

        FunctionCommandsLayout.addMultiCellLayout(layout8_2,3,3,0,1)

        self.textLabel1_2_2 = QLabel(self.FunctionCommands,"textLabel1_2_2")

        FunctionCommandsLayout.addMultiCellWidget(self.textLabel1_2_2,4,4,0,1)

        layout9 = QHBoxLayout(None,0,6,"layout9")

        self.ScanCommand = QLineEdit(self.FunctionCommands,"ScanCommand")
        layout9.addWidget(self.ScanCommand)

        FunctionCommandsLayout.addMultiCellLayout(layout9,5,5,0,1)

        self.textLabel1_2_3_3 = QLabel(self.FunctionCommands,"textLabel1_2_3_3")

        FunctionCommandsLayout.addMultiCellWidget(self.textLabel1_2_3_3,6,6,0,1)

        layout10_2 = QHBoxLayout(None,0,6,"layout10_2")

        self.AccessPCardCommand = QLineEdit(self.FunctionCommands,"AccessPCardCommand")
        layout10_2.addWidget(self.AccessPCardCommand)

        FunctionCommandsLayout.addMultiCellLayout(layout10_2,7,7,0,1)

        self.textLabel1_2_3 = QLabel(self.FunctionCommands,"textLabel1_2_3")
        self.textLabel1_2_3.setEnabled(1)

        FunctionCommandsLayout.addMultiCellWidget(self.textLabel1_2_3,8,8,0,1)

        layout11_2 = QHBoxLayout(None,0,6,"layout11_2")

        self.SendFaxCommand = QLineEdit(self.FunctionCommands,"SendFaxCommand")
        self.SendFaxCommand.setEnabled(1)
        layout11_2.addWidget(self.SendFaxCommand)

        FunctionCommandsLayout.addMultiCellLayout(layout11_2,9,9,0,1)

        self.textLabel1_2_3_2 = QLabel(self.FunctionCommands,"textLabel1_2_3_2")
        self.textLabel1_2_3_2.setEnabled(1)

        FunctionCommandsLayout.addMultiCellWidget(self.textLabel1_2_3_2,10,10,0,1)

        layout12_2 = QHBoxLayout(None,0,6,"layout12_2")

        self.MakeCopiesCommand = QLineEdit(self.FunctionCommands,"MakeCopiesCommand")
        self.MakeCopiesCommand.setEnabled(1)
        layout12_2.addWidget(self.MakeCopiesCommand)

        FunctionCommandsLayout.addMultiCellLayout(layout12_2,11,11,0,1)

        self.DefaultsButton = QPushButton(self.FunctionCommands,"DefaultsButton")
        self.DefaultsButton.setEnabled(1)

        FunctionCommandsLayout.addWidget(self.DefaultsButton,13,0)
        spacer8_2 = QSpacerItem(471,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        FunctionCommandsLayout.addItem(spacer8_2,13,1)
        spacer9 = QSpacerItem(20,81,QSizePolicy.Minimum,QSizePolicy.Expanding)
        FunctionCommandsLayout.addItem(spacer9,12,0)
        self.TabWidget.insertTab(self.FunctionCommands,QString.fromLatin1(""))

        SettingsDialog_baseLayout.addMultiCellWidget(self.TabWidget,0,0,0,2)

        self.languageChange()

        self.resize(QSize(627,481).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.pushButton31,SIGNAL("clicked()"),self.reject)
        self.connect(self.pushButton30,SIGNAL("clicked()"),self.accept)
        self.connect(self.EmailCheckBox,SIGNAL("toggled(bool)"),self.EmailAddress.setEnabled)
        self.connect(self.CleaningLevel,SIGNAL("clicked(int)"),self.CleaningLevel_clicked)
        self.connect(self.DefaultsButton,SIGNAL("clicked()"),self.DefaultsButton_clicked)
        self.connect(self.TabWidget,SIGNAL("currentChanged(QWidget*)"),self.TabWidget_currentChanged)
        self.connect(self.EmailTestButton,SIGNAL("clicked()"),self.EmailTestButton_clicked)
        self.connect(self.EmailCheckBox,SIGNAL("toggled(bool)"),self.senderLineEdit.setEnabled)
        self.connect(self.EmailCheckBox,SIGNAL("toggled(bool)"),self.EmailTestButton.setEnabled)
        self.connect(self.autoRefreshCheckBox,SIGNAL("clicked()"),self.autoRefreshCheckBox_clicked)
        self.connect(self.autoRefreshCheckBox,SIGNAL("toggled(bool)"),self.AutoRefreshRate.setEnabled)
        self.connect(self.autoRefreshCheckBox,SIGNAL("toggled(bool)"),self.radioButton1.setEnabled)
        self.connect(self.autoRefreshCheckBox,SIGNAL("toggled(bool)"),self.radioButton2.setEnabled)
        self.connect(self.refreshScopeButtonGroup,SIGNAL("clicked(int)"),self.refreshScopeButtonGroup_clicked)

        self.setTabOrder(self.TabWidget,self.pushButton30)
        self.setTabOrder(self.pushButton30,self.pushButton31)
        self.setTabOrder(self.pushButton31,self.EmailAddress)
        self.setTabOrder(self.EmailAddress,self.EmailCheckBox)
        self.setTabOrder(self.EmailCheckBox,self.EmailTestButton)
        self.setTabOrder(self.EmailTestButton,self.PrintCommand)
        self.setTabOrder(self.PrintCommand,self.ScanCommand)
        self.setTabOrder(self.ScanCommand,self.AccessPCardCommand)
        self.setTabOrder(self.AccessPCardCommand,self.SendFaxCommand)
        self.setTabOrder(self.SendFaxCommand,self.MakeCopiesCommand)
        self.setTabOrder(self.MakeCopiesCommand,self.DefaultsButton)


    def languageChange(self):
        self.setCaption(self.__tr("HP Device Manager - Settings"))
        self.pushButton30.setText(self.__tr("OK"))
        self.pushButton31.setText(self.__tr("Cancel"))
        self.textLabel3_2_2.setText(self.__tr("<b>Configure if and when device(s) are automatically refreshed</b>"))
        self.autoRefreshCheckBox.setText(self.__tr("Enable device auto refresh"))
        self.CleaningLevel.setTitle(self.__tr("Auto Interval"))
        self.textLabel1_4.setText(self.__tr("Refresh every:"))
        self.textLabel1_3.setText(self.__tr("minutes"))
        self.refreshScopeButtonGroup.setTitle(self.__tr("Device(s) to Refresh "))
        self.radioButton1.setText(self.__tr("Only currently selected device"))
        self.radioButton2.setText(self.__tr("All devices"))
        self.TabWidget.changeTab(self.CleaningLevels,self.__tr("Auto Refresh"))
        self.textLabel3_2.setText(self.__tr("<b>Configure if the HP Device Manager will send email on alerts</b>"))
        self.EmailCheckBox.setText(self.__tr("Send email when device errors occur:"))
        self.EmailTestButton.setText(self.__tr("Test"))
        self.groupBox1.setTitle(self.__tr("To: Address(es)"))
        self.textLabel20.setText(self.__tr("Email address(es):"))
        self.textLabel1.setText(self.__tr("<i>Note: Separate multiple email address with a commas.</i>"))
        self.groupBox2.setTitle(self.__tr("From: Address"))
        self.textLabel2.setText(self.__tr("Sender email address:"))
        self.textLabel3.setText(self.__tr("<i>Note: This should generally be your email address.</i>"))
        self.TabWidget.changeTab(self.EmailAlerts,self.__tr("Email Alerts"))
        self.textLabel3_2_2_2.setText(self.__tr("<b>Configure what commands to run for device functions</b>"))
        self.textLabel1_2.setText(self.__tr("Print Command:"))
        self.textLabel1_2_2.setText(self.__tr("Scan Command:"))
        self.textLabel1_2_3_3.setText(self.__tr("Access Photo Cards Command:"))
        self.textLabel1_2_3.setText(self.__tr("Send Fax Command:"))
        self.textLabel1_2_3_2.setText(self.__tr("Make Copies Command:"))
        self.DefaultsButton.setText(self.__tr("Set Defaults"))
        self.TabWidget.changeTab(self.FunctionCommands,self.__tr("Function Commands"))


    def PrintCmdChangeButton_clicked(self):
        print "SettingsDialog_base.PrintCmdChangeButton_clicked(): Not implemented yet"

    def ScanCmdChangeButton_clicked(self):
        print "SettingsDialog_base.ScanCmdChangeButton_clicked(): Not implemented yet"

    def AccessPCardCmdChangeButton_clicked(self):
        print "SettingsDialog_base.AccessPCardCmdChangeButton_clicked(): Not implemented yet"

    def SendFaxCmdChangeButton_clicked(self):
        print "SettingsDialog_base.SendFaxCmdChangeButton_clicked(): Not implemented yet"

    def MakeCopiesCmdChangeButton_clicked(self):
        print "SettingsDialog_base.MakeCopiesCmdChangeButton_clicked(): Not implemented yet"

    def CleaningLevel_clicked(self,a0):
        print "SettingsDialog_base.CleaningLevel_clicked(int): Not implemented yet"

    def pushButton5_clicked(self):
        print "SettingsDialog_base.pushButton5_clicked(): Not implemented yet"

    def DefaultsButton_clicked(self):
        print "SettingsDialog_base.DefaultsButton_clicked(): Not implemented yet"

    def TabWidget_currentChanged(self,a0):
        print "SettingsDialog_base.TabWidget_currentChanged(QWidget*): Not implemented yet"

    def pushButton6_clicked(self):
        print "SettingsDialog_base.pushButton6_clicked(): Not implemented yet"

    def EmailTestButton_clicked(self):
        print "SettingsDialog_base.EmailTestButton_clicked(): Not implemented yet"

    def autoRefreshCheckBox_clicked(self):
        print "SettingsDialog_base.autoRefreshCheckBox_clicked(): Not implemented yet"

    def refreshScopeButtonGroup_clicked(self,a0):
        print "SettingsDialog_base.refreshScopeButtonGroup_clicked(int): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("SettingsDialog_base",s,c)
