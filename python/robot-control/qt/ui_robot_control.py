# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'robot_control_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_RobotControl(object):
    def setupUi(self, RobotControl):
        RobotControl.setObjectName(_fromUtf8("RobotControl"))
        RobotControl.resize(815, 379)
        self.centralwidget = QtGui.QWidget(RobotControl)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 794, 311))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.monitorTitleLabel = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.monitorTitleLabel.setFont(font)
        self.monitorTitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.monitorTitleLabel.setObjectName(_fromUtf8("monitorTitleLabel"))
        self.gridLayout.addWidget(self.monitorTitleLabel, 0, 0, 1, 2)
        self.driveForwardButton = QtGui.QPushButton(self.widget)
        self.driveForwardButton.setObjectName(_fromUtf8("driveForwardButton"))
        self.gridLayout.addWidget(self.driveForwardButton, 3, 2, 1, 3)
        spacerItem = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 5, 1, 1)
        self.turnRightButton = QtGui.QPushButton(self.widget)
        self.turnRightButton.setObjectName(_fromUtf8("turnRightButton"))
        self.gridLayout.addWidget(self.turnRightButton, 2, 2, 1, 3)
        self.turnRightDistanceEntry = QtGui.QLineEdit(self.widget)
        self.turnRightDistanceEntry.setObjectName(_fromUtf8("turnRightDistanceEntry"))
        self.gridLayout.addWidget(self.turnRightDistanceEntry, 2, 5, 1, 2)
        self.sendCommandButton = QtGui.QPushButton(self.widget)
        self.sendCommandButton.setObjectName(_fromUtf8("sendCommandButton"))
        self.gridLayout.addWidget(self.sendCommandButton, 6, 2, 1, 3)
        self.turnLeftButton = QtGui.QPushButton(self.widget)
        self.turnLeftButton.setObjectName(_fromUtf8("turnLeftButton"))
        self.gridLayout.addWidget(self.turnLeftButton, 1, 2, 1, 3)
        self.driveForwardDistanceEntry = QtGui.QLineEdit(self.widget)
        self.driveForwardDistanceEntry.setObjectName(_fromUtf8("driveForwardDistanceEntry"))
        self.gridLayout.addWidget(self.driveForwardDistanceEntry, 3, 5, 1, 2)
        self.clearCommandButton = QtGui.QPushButton(self.widget)
        self.clearCommandButton.setObjectName(_fromUtf8("clearCommandButton"))
        self.gridLayout.addWidget(self.clearCommandButton, 6, 6, 1, 1)
        self.driveBackwardsButton = QtGui.QPushButton(self.widget)
        self.driveBackwardsButton.setObjectName(_fromUtf8("driveBackwardsButton"))
        self.gridLayout.addWidget(self.driveBackwardsButton, 4, 2, 1, 3)
        self.driveBackwardsDistanceEntry = QtGui.QLineEdit(self.widget)
        self.driveBackwardsDistanceEntry.setObjectName(_fromUtf8("driveBackwardsDistanceEntry"))
        self.gridLayout.addWidget(self.driveBackwardsDistanceEntry, 4, 5, 1, 2)
        self.turnLeftDistanceEntry = QtGui.QLineEdit(self.widget)
        self.turnLeftDistanceEntry.setObjectName(_fromUtf8("turnLeftDistanceEntry"))
        self.gridLayout.addWidget(self.turnLeftDistanceEntry, 1, 5, 1, 2)
        self.recordButton = QtGui.QPushButton(self.widget)
        self.recordButton.setObjectName(_fromUtf8("recordButton"))
        self.gridLayout.addWidget(self.recordButton, 5, 2, 1, 3)
        self.playRecordingButton = QtGui.QPushButton(self.widget)
        self.playRecordingButton.setObjectName(_fromUtf8("playRecordingButton"))
        self.gridLayout.addWidget(self.playRecordingButton, 5, 6, 1, 1)
        self.movementControlLabel = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.movementControlLabel.setFont(font)
        self.movementControlLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.movementControlLabel.setObjectName(_fromUtf8("movementControlLabel"))
        self.gridLayout.addWidget(self.movementControlLabel, 0, 2, 1, 5)
        self.monitor = QtGui.QLabel(self.widget)
        self.monitor.setFrameShape(QtGui.QFrame.WinPanel)
        self.monitor.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.monitor.setObjectName(_fromUtf8("monitor"))
        self.gridLayout.addWidget(self.monitor, 1, 0, 5, 2)
        self.sequenceText = QtGui.QTextEdit(self.widget)
        self.sequenceText.setObjectName(_fromUtf8("sequenceText"))
        self.gridLayout.addWidget(self.sequenceText, 7, 2, 2, 5)
        self.importCommandButton = QtGui.QPushButton(self.widget)
        self.importCommandButton.setObjectName(_fromUtf8("importCommandButton"))
        self.gridLayout.addWidget(self.importCommandButton, 7, 0, 1, 2)
        self.saveCommandButton = QtGui.QPushButton(self.widget)
        self.saveCommandButton.setObjectName(_fromUtf8("saveCommandButton"))
        self.gridLayout.addWidget(self.saveCommandButton, 8, 0, 1, 2)
        RobotControl.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(RobotControl)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 815, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        RobotControl.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(RobotControl)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        RobotControl.setStatusBar(self.statusbar)
        self.actionImport_Control_Sequence = QtGui.QAction(RobotControl)
        self.actionImport_Control_Sequence.setObjectName(_fromUtf8("actionImport_Control_Sequence"))
        self.actionSave_Control_Sequence = QtGui.QAction(RobotControl)
        self.actionSave_Control_Sequence.setObjectName(_fromUtf8("actionSave_Control_Sequence"))
        self.actionExit = QtGui.QAction(RobotControl)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionImport_Control_Sequence)
        self.menuFile.addAction(self.actionSave_Control_Sequence)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(RobotControl)
        QtCore.QMetaObject.connectSlotsByName(RobotControl)
        RobotControl.setTabOrder(self.turnLeftButton, self.turnLeftDistanceEntry)
        RobotControl.setTabOrder(self.turnLeftDistanceEntry, self.turnRightButton)
        RobotControl.setTabOrder(self.turnRightButton, self.turnRightDistanceEntry)
        RobotControl.setTabOrder(self.turnRightDistanceEntry, self.driveForwardButton)
        RobotControl.setTabOrder(self.driveForwardButton, self.driveForwardDistanceEntry)
        RobotControl.setTabOrder(self.driveForwardDistanceEntry, self.driveBackwardsButton)
        RobotControl.setTabOrder(self.driveBackwardsButton, self.driveBackwardsDistanceEntry)
        RobotControl.setTabOrder(self.driveBackwardsDistanceEntry, self.recordButton)
        RobotControl.setTabOrder(self.recordButton, self.playRecordingButton)
        RobotControl.setTabOrder(self.playRecordingButton, self.sendCommandButton)
        RobotControl.setTabOrder(self.sendCommandButton, self.clearCommandButton)
        RobotControl.setTabOrder(self.clearCommandButton, self.importCommandButton)
        RobotControl.setTabOrder(self.importCommandButton, self.saveCommandButton)
        RobotControl.setTabOrder(self.saveCommandButton, self.sequenceText)

    def retranslateUi(self, RobotControl):
        RobotControl.setWindowTitle(_translate("RobotControl", "Robot Control Graphical Interface", None))
        self.monitorTitleLabel.setText(_translate("RobotControl", "Robot Monitor", None))
        self.driveForwardButton.setText(_translate("RobotControl", "Drive Forward", None))
        self.turnRightButton.setText(_translate("RobotControl", "Turn Right", None))
        self.sendCommandButton.setText(_translate("RobotControl", "Send Command Sequence", None))
        self.turnLeftButton.setText(_translate("RobotControl", "Turn Left", None))
        self.clearCommandButton.setText(_translate("RobotControl", "Clear Command Sequence", None))
        self.driveBackwardsButton.setText(_translate("RobotControl", "Drive Backwards", None))
        self.recordButton.setText(_translate("RobotControl", "Start Recording", None))
        self.playRecordingButton.setText(_translate("RobotControl", "Play Recording", None))
        self.movementControlLabel.setText(_translate("RobotControl", "Movement Control", None))
        self.monitor.setText(_translate("RobotControl", "Left wheel speed:   2cm/s\n"
"Right wheel speed:  2cm/s\n"
"Left wheel pulses:  30 pulse/s\n"
"Right wheel pulses: 30 pulse/s\n"
"Measured distance:  2m\n"
"Wii pad status:     x=2 y=4 z=6\n"
"PWM percentage:     30%\n"
"IP address:         192.10.20.50", None))
        self.importCommandButton.setText(_translate("RobotControl", "Import Command Sequence", None))
        self.saveCommandButton.setText(_translate("RobotControl", "Save Command Sequence", None))
        self.menuFile.setTitle(_translate("RobotControl", "File", None))
        self.menuAbout.setTitle(_translate("RobotControl", "About", None))
        self.actionImport_Control_Sequence.setText(_translate("RobotControl", "&Import Control Sequence", None))
        self.actionSave_Control_Sequence.setText(_translate("RobotControl", "Save Control Sequence", None))
        self.actionExit.setText(_translate("RobotControl", "Exit", None))

