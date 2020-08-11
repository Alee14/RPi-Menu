# RPI Menu
Basically a full screen program menu. Meant for Raspberry Pi OS.

I recommend you putting this repo on your home folder under the name `menu`. (/home/pi)

# Requirements
- Python 3+
- Tkinter 8+
- Kodi
- Steam Link
- [Retropie](https://retropie.org.uk/docs/Manual-Installation/)
- [Mycroft AI](https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/get-mycroft/linux) (Optional) (Must clone it on the home folder)

# Putting this on startup
If you want to make this python app autostart when xserver is started do the following

Edit `/etc/xdg/lxsession/LXDE-pi/autostart`

Add the following command in the bottom `/usr/bin/python3 /home/pi/menu/menu.py`

# Debugging
If you're using SSH (recommended). You need to execute `run.sh`.