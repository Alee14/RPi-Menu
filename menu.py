#!/usr/bin/env python3
"""
    RPi Menu
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
root = tkinter.Tk()
root.attributes('-fullscreen', True)
root.title("Startup GUI")
root['background']='#4d4d4d'
print("RPi Menu Copyright (C) 2020 Andrew Lee\nThis program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.\nThis is free software, and you are welcome to redistribute it\nunder certain conditions; type `show c' for details.\n")

print("Starting Startup GUI")

print("Tkinter Version:" , tkinter.TkVersion)

# Functions
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
    # TODO: Fix this
    os.system("emulationstation")
    quit()
def launchSteam():
    print("Launching Steam Link")
    os.system("steamlink &")
    quit()
def launchKodi():
    print("Launching Kodi")
    os.system("kodi &")
    quit()

# Labels
labelFont = tkFont.Font(size=15)
varWelcome = StringVar()
labelWelcome = Label( root, textvariable=varWelcome, font=labelFont, bg="#4d4d4d", fg="white")
varWelcome.set("Welcome to Raspberry Pi OS!\nWhere do you want to go?\n")

varCopyright = StringVar()
labelCopyright = Label( root, textvariable=varCopyright, font=labelFont, bg="#4d4d4d", fg="white")
varCopyright.set("(C) Copyright 2020, Andrew Lee. Licensed with GPL-3.0\nhttps://alee14.me")

# Buttons
btnFont = tkFont.Font(size=12, weight="bold")
btnDesktop = Button(root, text = 'Desktop', width=60, height=3, font=btnFont, bg="#8c8c8c", activebackground="#666666", bd=0, relief="flat", command = launchDesktop) 
btnDashboard = Button(root, text = 'Dashboard + Mycroft AI', width=60, height=3, font=btnFont, bg="#8c8c8c", activebackground="#666666", bd=0, relief="flat", command = launchDashboard) 
btnRetroPie = Button(root, text = 'RetroPie', width=60, height=3, font=btnFont, bg="#8c8c8c", activebackground="#666666", bd=0, relief="flat", command = launchRetroPie) 
btnSteamLink = Button(root, text = 'Steam Link', width=60, height=3, font=btnFont, bg="#8c8c8c", activebackground="#666666", bd=0, relief="flat", command = launchSteam)
btnKodi = Button(root, text = 'Kodi', width=60, height=3, font=btnFont, bg="#8c8c8c", activebackground="#666666", relief="flat", bd=0, command = launchKodi) 

# Add the stuff
labelWelcome.pack()
btnDesktop.pack()
btnDashboard.pack()
btnRetroPie.pack()
btnSteamLink.pack()
btnKodi.pack()
labelCopyright.pack()

# Run the app
root.mainloop()
