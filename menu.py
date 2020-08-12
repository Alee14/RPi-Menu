#!/usr/bin/env python3
"""
    Raspberry Pi OS Menu: Where do you want to go today?
    Copyright (C) 2020 Andrew Lee

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import tkinter
import os
from tkinter import *
from tkinter import font as tkFont
from tkinter import messagebox
app = tkinter.Tk()

# Functions
def msgbox():
    msgboxMessage = messagebox.showinfo(title="Information", message="This option is currently broken.")
    Label(app, text=msgboxMessage).pack()
def launchDesktop():
    print("Launching Desktop")
    quit()
def launchDashboard():
    print("Launching Dashboard")
    os.system("nohup /home/pi/menu/startDash.sh &")
    #os.system("bash /home/pi/menu/dashboard.sh &")
    quit()
def launchRetroPie():
    print("Launching RetroPie")
    #os.system("nohup sudo su -c \"systemctl stop lightdm ; ttyecho -n /dev/tty1 \"emulationstation ; sudo systemctl start lightdm\"\"")
    #os.system("nohup sudo pkill Xorg ; emulationstation")
    #os.system("nohup /home/pi/menu/launchES.sh")
    msgbox()
    #quit()
def launchSteam():
    print("Launching Steam Link")
    os.system("/usr/bin/steamlink &")
    quit()
def launchKodi():
    print("Launching Kodi")
    os.system("/usr/bin/kodi &")
    quit()

# Variables
appName = "Raspberry Pi OS Menu"
appBackground = "#4d4d4d"
btnSizeW = 60
btnSizeH = 3
btnBG = "#8c8c8c"
btnABG = "#666666"
btnBD = 0
btnRelief = "flat"
labelFont = tkFont.Font(size=15, weight="bold")
btnFont = tkFont.Font(size=12, weight="bold")

print(appName + " Copyright (C) 2020 Andrew Lee\nThis program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.\nThis is free software, and you are welcome to redistribute it\nunder certain conditions; type `show c' for details.\n")
print("Starting " + appName)
print("Tkinter Version:" , tkinter.TkVersion)
app.attributes('-fullscreen', True)
app.title(appName)
app.configure(bg=appBackground)

# Labels
varWelcome = StringVar()
labelWelcome = Label( app, textvariable=varWelcome, font=labelFont, bg=appBackground, fg="white")
varWelcome.set("Welcome to Raspberry Pi OS!\nWhere do you want to go today?\n")

varCopyright = StringVar()
labelCopyright = Label( app, textvariable=varCopyright, font=labelFont, bg=appBackground, fg="white")
varCopyright.set("(C) Copyright 2020, Andrew Lee. Licensed with GPL-3.0\nhttps://alee14.me")

# Buttons
btnDesktop = Button(app, text = 'Desktop', width=btnSizeW, height=btnSizeH, font=btnFont, bg=btnBG, activebackground=btnABG, bd=btnBD, relief=btnRelief, command = launchDesktop) 
btnDashboard = Button(app, text = 'Dashboard + Mycroft AI', width=btnSizeW, height=btnSizeH, font=btnFont, bg=btnBG, activebackground=btnABG, bd=btnBD, relief=btnRelief, command = launchDashboard) 
btnRetroPie = Button(app, text = 'RetroPie', width=btnSizeW, height=btnSizeH, font=btnFont, bg=btnBG, activebackground=btnABG, bd=btnBD, relief=btnRelief, command = launchRetroPie) 
btnSteamLink = Button(app, text = 'Steam Link', width=btnSizeW, height=btnSizeH, font=btnFont, bg=btnBG, activebackground=btnABG, bd=btnBD, relief=btnRelief, command = launchSteam)
btnKodi = Button(app, text = 'Kodi', width=btnSizeW, height=btnSizeH, font=btnFont, bg=btnBG, activebackground=btnABG, relief=btnRelief, bd=btnBD, command = launchKodi) 

# Add the components
labelWelcome.pack()
btnDesktop.pack()
btnDashboard.pack()
btnRetroPie.pack()
btnSteamLink.pack()
btnKodi.pack()
labelCopyright.pack()

# Run the app
app.mainloop()
