#!/bin/bash

sudo cp -v robot_control.py /usr/bin
desktopVar=$(cat $HOME/.config/user-dirs.dirs | grep "XDG_DESKTOP_DIR")
desktopFolder=$(echo ${desktopVar/XDG_DESKTOP_DIR=/""} | tr -d '"' | cut -d'/' -f 2)
echo '#!/usr/bin/env xdg-open
[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Icon[en_US]=remmina
Name[en_US]=Robot Control App
Exec=/usr/bin/python /usr/bin/robot_control.py
Path=/usr/bin/
Comment[en_US]=Launcher for the Robot Control application
Name=Robot Control App
Comment=Launcher for the Robot Control application
Icon=remmina
StartupNotify=true
Categories=Utility;Application;
StartupWMClass=tk
' > ~/$desktopFolder/robot_control_app.desktop #Add shortcut to desktop.
sudo cp -v ~/$desktopFolder/robot_control_app.desktop /usr/share/applications #Add shortcut to the launcher (/usr/share/applications/)
chmod +x ~/$desktopFolder/robot_control_app.desktop
