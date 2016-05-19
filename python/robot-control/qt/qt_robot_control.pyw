#!/usr/bin/env python

import re
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_robot_control

class RobotControl(QMainWindow,
                        ui_robot_control.Ui_RobotControl):
    def __init__(self, parent=None):
        super(RobotControl, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    form = RobotControl()
    form.show()
    app.exec_()

if __name__ ==  "__main__":
    main()

