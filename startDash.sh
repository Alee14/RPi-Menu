#!/bin/bash
pulseaudio --start
bash /home/pi/mycroft-core/start-mycroft.sh all &
bash /home/pi/menu/dashboard.sh
bash /home/pi/mycroft-core/stop-mycroft.sh
