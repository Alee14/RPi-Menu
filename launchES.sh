#!/bin/bash
sudo pkill Xorg &
emulationstation
su pi ; DISPLAY=:0.0 startx &