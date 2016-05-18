#!/usr/bin/env python

import re
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_robot_control

class RobotControl(QDialog,
                        ui_robot_control.Ui_RobotControl):
    def __init__(self, text, parent=None):
        super(RobotControl, self).__init__(parent)
        self.__text = unicode(text)
        self.__index = 0
        self.setupUi(self)
        self.updateUi()

def main():
    robotcontrol = RobotControl()


if __name__ ==  "__main__":
    main()

