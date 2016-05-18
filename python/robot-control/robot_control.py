#!/usr/bin/env python

import subprocess
import os
import time
import sys
#from timer import timer
from Tkinter import *
import tkFileDialog

ABOUT_TEXT = """ This application is a remote control for the spy robot. It has
been programmed with python 2.7 and Tkinter GUI. """

#Hide the traced in stderr:
#old_stdout = sys.stderr
#sys.stderr = open(os.devnull, 'w')

class gen_App_GUI:
    command_string = '' #Main command string to send over bluetooth.
    def __init__(self, root, width, height):
        self.root = root
        self.root.title('Robot Control Graphical Interface')
        self.set_window_pos(self.root, width, height)
        self.root.bind("<Button-1>", self.setFocusMainWindow_callback)
        #self.frame = Frame(self.root)
        #self.frame.grid()
        self.menubar = Menu(self.root)
        #File menu and submenu
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Import Control Sequence",
                                  command=self.importControlSequence_Menu)
        self.filemenu.add_command(label="Save Control Sequence",
                                  command=self.saveControlSequence_Menu)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.root.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_command(label="About", command=self.about_Menu)
        self.root.config(menu=self.menubar) #To show manubar
        
        # define options for opening or saving a file:
        self.file_opt = options = {}
        options['defaultextension'] = '.txt'
        options['filetypes'] = [('text files', '.txt'), ('all files', '.*')]
        options['initialdir'] = '~/'
        options['initialfile'] = 'control_sequence.txt'
        options['parent'] = self.root
        options['title'] = 'Import/Save Control Sequence from/to file'

        #App main layout:
        monitorTitleLabel = Label(self.root, padx=3, text="Robot Monitor",
                                    font=("Helvetica", 10, "bold"))
        monitorTitleLabel.grid(row=0, columnspan=2)
        self.params_info_variable = StringVar()
        self.get_robot_params_info()
        monitor = Label(self.root, height=10, padx=20, justify=LEFT,
                        anchor=CENTER, relief=GROOVE,  
                        textvariable=self.params_info_variable)
        monitor.grid(column=0, rowspan=5, columnspan=2,  sticky=W+E+N+S)
        movementControlLabel = Label(self.root, padx=10, justify=CENTER, 
                                       text="Movement Control",
                                       font=("Helvetica", 10, "bold"))
        movementControlLabel.grid(column=2, row=0, columnspan=2)
        # -------------------- Turn Left section: ------------------- #
        turnLeftButton = Button(self.root, text="Turn Left", 
                                  command=self.turnLeftButton_callback)
        turnLeftButton.grid(column=2, row=1, sticky=W+E)
        self.turnLeftDistanceVar = IntVar()
        self.turnLeftDistanceEntry = Entry(self.root,
                                          textvariable=self.turnLeftDistanceVar)
        self.turnLeftDistanceEntry.delete(0, END)
        self.turnLeftDistanceEntry.insert(0, "Distance (3 digits in cm)")
        self.turnLeftDistanceEntry.config(foreground="grey")
        #When the mouse left button is pressed over the text entry 
        #the entry is cleared:
        self.turnLeftDistanceEntry.bind("<Button-1>", lambda event, 
                                         widget=self.turnLeftDistanceEntry,
                                         distanceVar=self.turnLeftDistanceVar:
                                         self.entryClear_callback(widget, distanceVar))
        self.turnLeftDistanceEntry.bind("<FocusOut>", lambda event,
                                        widget=self.turnLeftDistanceEntry,
                                        distanceVar=self.turnLeftDistanceVar:
                                        self.entryReset_callback(widget, distanceVar))
        self.turnLeftDistanceEntry.grid(column=3, row=1, sticky=W+E)
        # -------------------- Turn Right section: ------------------ #
        turnRightButton = Button(self.root, text="Turn Right", 
                                   command=self.turnRightButton_callback)
        turnRightButton.grid(column=2, row=2, sticky=W+E)
        self.turnRightDistanceVar = IntVar()
        self.turnRightDistanceEntry = Entry(self.root,
                                          textvariable=self.turnRightDistanceVar)
        self.turnRightDistanceEntry.delete(0, END)
        self.turnRightDistanceEntry.insert(0, "Distance (3 digits in cm)")
        self.turnRightDistanceEntry.config(foreground="grey")
        #When the mouse left button is pressed over the text entry 
        #the entry is cleared:
        self.turnRightDistanceEntry.bind("<Button-1>", lambda event, 
                                         widget=self.turnRightDistanceEntry, 
                                         distanceVar=self.turnRightDistanceVar:
                                         self.entryClear_callback(widget, distanceVar))
        self.turnRightDistanceEntry.bind("<FocusOut>", lambda event,
                                        widget=self.turnRightDistanceEntry,
                                        distanceVar=self.turnRightDistanceVar:
                                        self.entryReset_callback(widget, distanceVar))
        self.turnRightDistanceEntry.grid(column=3, row=2, sticky=W+E)
        # ------------------ Drive Forward section: ----------------- #
        driveForwardButton = Button(self.root, text="Drive Forward",
                                    command=self.driveForwardButton_callback)
        driveForwardButton.grid(column=2, row=3, sticky=W+E)
        self.driveForwardDistanceVar = IntVar()
        self.driveForwardDistanceEntry = Entry(self.root,
                                          textvariable=self.driveForwardDistanceVar)
        self.driveForwardDistanceEntry.delete(0, END)
        self.driveForwardDistanceEntry.insert(0, "Distance (3 digits in cm)")
        self.driveForwardDistanceEntry.config(foreground="grey")
        #When the mouse left button is pressed over the text entry 
        #the entry is cleared:
        self.driveForwardDistanceEntry.bind("<Button-1>", lambda event, 
                                            widget=self.driveForwardDistanceEntry,
                                            distanceVar=self.driveForwardDistanceVar:
                                            self.entryClear_callback(widget, distanceVar))
        self.driveForwardDistanceEntry.bind("<FocusOut>", lambda event,
                                        widget=self.driveForwardDistanceEntry,
                                        distanceVar=self.driveForwardDistanceVar:
                                        self.entryReset_callback(widget, distanceVar))
        self.driveForwardDistanceEntry.grid(column=3, row=3, sticky=W+E)
        # ------------------ Drive Backwards section: ----------------- #
        driveBackwardsButton = Button(self.root, text="Drive Backwards",
                                    command=self.driveBackwardsButton_callback)
        driveBackwardsButton.grid(column=2, row=4, sticky=W+E)
        self.driveBackwardsDistanceVar = IntVar()
        self.driveBackwardsDistanceEntry = Entry(self.root,
                                          textvariable=self.driveBackwardsDistanceVar)
        self.driveBackwardsDistanceEntry.delete(0, END)
        self.driveBackwardsDistanceEntry.insert(0, "Distance (3 digits in cm)")
        self.driveBackwardsDistanceEntry.config(foreground="grey")
        #When the mouse left button is pressed over the text entry 
        #the entry is cleared:
        self.driveBackwardsDistanceEntry.bind("<Button-1>", lambda event, 
                                              widget=self.driveBackwardsDistanceEntry,
                                              distanceVar=self.driveBackwardsDistanceVar:
                                              self.entryClear_callback(widget, distanceVar)) 
        self.driveBackwardsDistanceEntry.bind("<FocusOut>", lambda event,
                                        widget=self.driveBackwardsDistanceEntry,
                                        distanceVar=self.driveBackwardsDistanceVar:
                                        self.entryReset_callback(widget, distanceVar))
        self.driveBackwardsDistanceEntry.grid(column=3, row=4, sticky=W+E)
        # ----------------------------------------------------------- #
        self.recordButton = Button(self.root, text="Start Recording",
                              command=self.recordButton_callback)
        self.recordButton.grid(column=2, row=5, sticky=W+E)
        self.playRecordingButton = Button(self.root, text="Play Recording",
                                          command=self.playRecordingButton_callback)
        self.playRecordingButton.grid(column=3, row=5, sticky=W+E)
        # ----------------------------------------------------------- #
        self.sendCommandButton = Button(self.root, text="Send Commands",
                                   command=self.sendCommandButton_callback)
        self.sendCommandButton.grid(column=2, row=6, sticky=W+E, pady=10)
        self.clearCommandButton = Button(self.root, text="Clear Commands",
                                   command=self.clearCommandButton_callback)
        self.clearCommandButton.grid(column=3, row=6, sticky=W+E, pady=10)
        # ----------------------------------------------------------- #
        self.sequenceLabel = Label(self.root, text="Control Sequence",
                                   font=("Helvetica", 10, "bold"))
        self.sequenceLabel.grid(column=0, row=11, columnspan=4)
        self.importControlSequenceButton = Button(self.root, text="Import Sequence",
                                                command=self.importControlSequenceButton_callback)
        self.importControlSequenceButton.grid(column=0, row=12, sticky=W+E)
        self.saveControlSequenceButton = Button(self.root, text="Save Sequence",
                                                command=self.saveControlSequenceButton_callback)
        self.saveControlSequenceButton.grid(column=0, row=13, sticky=W+E)
        self.sequenceText = Text(self.root, height=2)
        self.sequenceText.delete(1.0, END)
        self.sequenceText.grid(column=1, row=12, rowspan=2, columnspan=3, sticky=W+E+N+S)
        
    def about_Menu(self):
        self.about_window = about_window = Toplevel()
        about_window.title('About')
        about_window.focus_force() #To force the focus to this window.
        about_window.wm_attributes("-topmost", 1) #Keep this window on top till it is closed.
        about_window.grab_set() #To be able to only interact with the About window.
        self.set_window_pos(about_window, 375, 80)
        label_about = Label(about_window, text=ABOUT_TEXT, height=2,
                            justify=CENTER, anchor=CENTER)
        label_about.grid(column=0, row=0, sticky=W+E, pady=5)
        button_OK = Button(about_window, text="OK", width=10, command=self.about_Menu_close)
        button_OK.grid(column=0, row=1, pady=2, sticky=N)

    def about_Menu_close(self):
        self.about_window.grab_release()
        self.about_window.destroy()

    def importControlSequence_Menu(self):
        filename = tkFileDialog.askopenfilename(**self.file_opt)
        if filename:
            f = open(filename, "r")
            self.command_string = f.read()
            self.printSequenceText(self.command_string)
            f.close()

    def saveControlSequence_Menu(self):
        filename = tkFileDialog.asksaveasfilename(**self.file_opt)
        if filename:
            f = open(filename, "w")
            f.write(self.command_string)
            f.close()

    def set_window_pos(self, window, width=800, height=600):
        # get screen width and height
        width_screen = window.winfo_screenwidth() # width of the screen
        height_screen = window.winfo_screenheight() # height of the screen
        # calculate x and y coordinates for the Tk root window
        x = (width_screen/2) - (width/2)
        y = (height_screen/2) - (height/2)
        # set the dimensions of the screen 
        # and where it is placed
        window.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def get_robot_params_info(self):
        text = """Left wheel speed:   2cm/s
Right wheel speed:  2cm/s
Left wheel pulses:  30 pulse/s
Right wheel pulses: 30 pulse/s
Measured distance:  2m
Wii pad status:     x=2 y=4 z=6
PWM percentage:     30%
IP address:         192.10.20.50"""
        self.params_info_variable.set(text)
        check_period = 500 #ms
        self.root.after(check_period, self.get_robot_params_info)

    def entryClear_callback(event, entryName, distanceVar): #Event=Click
        try:
            distanceVar.get() #If the distanceVar is a number then no need to
                              #clean the text entry.
        except ValueError:
            entryName.delete(0, END)
            entryName.config(foreground="black")
            entryName.focus_set()

    def entryReset_callback(event, entryName, distanceVar): #Event=Focus Out
        try:
            distanceVar.get()
        except ValueError:
            entryName.delete(0, END)
            entryName.config(foreground="grey")
            entryName.insert(0, "Distance (3 digits in cm)")

    def turnLeftButton_callback(self):
        try:
            turnLeftDistance = self.turnLeftDistanceVar.get()
        except ValueError:
            error_text = 'Error, the distance must be an integer'
            self.error_Window(error_text)
            return -1
        if turnLeftDistance < 1 or turnLeftDistance > 500:
            error_text = 'Error, the distance must be between 1 and 500 (cm)'
            self.error_Window(error_text)
        elif self.checkEndSequence() != 'end_of_sequence':
            self.command_string += "I" + str('%03d' % self.turnLeftDistanceVar.get())
        else:
            self.error_Window("The sequence is complete (0x0D at the end)")
        self.printSequenceText(self.command_string)

    def turnRightButton_callback(self):
        try:
            turnRightDistance = self.turnRightDistanceVar.get()
        except ValueError:
            error_text = 'Error, the distance must be an integer'
            self.error_Window(error_text)
            return -1
        if turnRightDistance < 1 or turnRightDistance > 500:
            error_text = 'Error, the distance must be between 1 and 500 (cm)'
            self.error_Window(error_text)
        elif self.checkEndSequence() != 'end_of_sequence':
            self.command_string += "D" + str('%03d' % self.turnRightDistanceVar.get())
        else:
            self.error_Window("The sequence is complete (0x0D at the end)")
        self.printSequenceText(self.command_string)

    def driveForwardButton_callback(self):
        try:
            forwardDistance = self.driveForwardDistanceVar.get()
        except ValueError:
            error_text = 'Error, the distance must be an integer'
            self.error_Window(error_text)
            return -1
        if forwardDistance < 1 or forwardDistance > 500:
            error_text = 'Error, the distance must be between 1 and 500 (cm)'
            self.error_Window(error_text)
        elif self.checkEndSequence() != 'end_of_sequence':
            self.command_string += "A" +  str('%03d' % self.driveForwardDistanceVar.get())
        else:
            self.error_Window("The sequence is complete (0x0D at the end)")
        self.printSequenceText(self.command_string)

    def driveBackwardsButton_callback(self):
        try:
            backwardsDistance = self.driveBackwardsDistanceVar.get()
        except ValueError:
            error_text = 'Error, the distance must an integer'
            self.error_Window(error_text)
            return -1
        if backwardsDistance < 1 or backwardsDistance > 500:
            error_text = 'Error, the distance must be between 1 and 500 (cm)'
            self.error_Window(error_text)
        elif self.checkEndSequence() != 'end_of_sequence':
            self.command_string += "R" +  str('%03d' % self.driveBackwardsDistanceVar.get())
        else:
            self.error_Window("The sequence is complete (0x0D at the end)")
        self.printSequenceText(self.command_string)

    def recordButton_callback(self):
        if self.checkEndSequence() != 'end_of_sequence':
            self.command_string += "G"
            self.printSequenceText(self.command_string)
        else:
            self.error_Window("The sequence is complete (0x0D at the end)")

    def playRecordingButton_callback(self):
        for letter in self.command_string:
            if letter == 'G':
                if self.checkEndSequence() != 'end_of_sequence':
                    self.command_string += "E"
                    self.printSequenceText(self.command_string)
                    return 0
                else:
                    self.error_Window("The sequence is complete (0x0D at the end)")
                    return 0
        self.error_Window("There is no recorded data")

    def sendCommandButton_callback(self):
        if self.command_string != '':
            if self.checkEndSequence() == 'end_of_sequence': #If the last letter is D then:
                #sendOverBluetooth()
                return 0
            self.command_string += "0D" #Indicates the end of the transmission sequence.
            self.printSequenceText(self.command_string)
            #sendOverBluetooth()
        else:
            self.error_Window("There is no command to send") 
   
    def clearCommandButton_callback(self):
        self.command_string = ''
        self.clearSequenceText()

    def importControlSequenceButton_callback(self):
        self.importControlSequence_Menu()

    def saveControlSequenceButton_callback(self):
        self.saveControlSequence_Menu()

    def printSequenceText(self, command_string):
        self.sequenceText.delete(1.0, END)
        self.sequenceText.insert(INSERT, command_string)

    def clearSequenceText(self):
        self.sequenceText.delete(1.0, END)

    def error_Window(self, error_text):
        self.error_window = error_window = Toplevel()
        error_window.title('Error')
        error_window.focus_force() #To force the focus to this window.
        error_window.wm_attributes("-topmost", 1) #Keep this window on top till it is closed.
        error_window.grab_set() #To be able to only interact with the Error window.
        self.set_window_pos(self.error_window, 360, 70)
        label_error = Label(error_window, text=error_text,
                            justify=CENTER, anchor=CENTER, width=45)
        label_error.grid(row=0, sticky=W+E+N+S, pady=5)
        button_OK = Button(error_window, text="OK", width=5, 
                           command=self.error_Window_close)
        button_OK.grid(row=1, pady=2, sticky=N)

    def error_Window_close(self):
        self.error_window.grab_release()
        self.error_window.destroy()

    def setFocusMainWindow_callback(self, event):
        event.widget.focus_set()

    def checkEndSequence(self):
        if self.command_string[-1] == 'D': #If the last letter is D then:
            return 'end_of_sequence'
        else:
            return 0

def main():
    root = Tk()
    main_GUI = gen_App_GUI(root, 705, 300) #800x600
    root.mainloop()

if __name__ == "__main__":
    main()

# End of the script.
