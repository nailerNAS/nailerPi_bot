# nailerPi_bot

# Linux requirements:
  * etherwake
  * python3
  * pip3 (Optional, needed for easy installation of pyTelegramBotAPI lib)
  * screen (Optional, needed for screen.sh script to work; recommended anyways)
  
  Raspbian/Ubuntu/Debian derivatives:\
    ```sudo apt update && sudo apt install python3 etherwake python3-pip screen -y```

# Python requirements:
  * pyTelegramBotAPI
  
  If you have pip3 installed (python3-pip):
    ```pip3 install --user pytelegrambotapi``` <--Recommended\
    or\
    ```sudo pip3 install pytelegrambotapi``` <--Installs the lib system-wide

# config.py
  Modify this file with **your own** Bot Token [@BotFather](https://telegram.me/botfather)\
  Use **your** Telegram account ID [@getidsbot](https://telegram.me/getidsbot)\
  Use **your own** MAC address and interface names (on Raspbian you don't need to change interface names)\
  \
  Additionally you can change buttons text in main.py at the beginning

# Startup
  There are two scripts: start.sh and screen.sh
  * start.sh launches the bot and restarts it in case if bot stops for any reason (like unhandled exception)
  * screen.sh simply launches start.sh in the background by using Linux screen. You can reattach to that background console session by running ```screen -r nailerpi```. The ```nailerpi``` name of screen can be modified in screen.sh
  
  To make your bot start automatically on boot, run ```crontab -e``` and add this to last line:\
    ```@reboot sh /home/pi/nailerpi/screen.sh >/dev/null 2>&1```\
    where */home/pi/nailerpi* is path to your bot

# Startup - a better way
  The better way of running your bot at startup is by running him as a service

  Create a new service file:
  ```sudo nano /etc/systemd/system/nailerpi.service```\
  The content should look like this:
```
[Unit]
After=network.target
Description=nailerPi Telegram Bot for simple controls

[Service]
Type=simple
ExecStart=/home/pi/nailerpi/env/bin/python main.py
WorkingDirectory=/home/pi/nailerpi
User=pi
Restart=always

[Install]
WantedBy=multi-user.target
```
Replace the pythonpath with your own, for example ```/usr/bin/python3```\
Also change the working directory to the one where you've downloaded the bot (where the **<span>main.py</span>** file is)\
\
After creating this file, run these commands:
  ```
  sudo systemctl daemon-reload
  sudo systemctl enable nailerpi
  ```
If everything's good, your bot will now start automatically when your system boots, restart automatically upon crashes. To launch him right away (or relaunch) you can use
```
sudo systemctl restart nailerpi
```

If you're using SystemD instead of cron, you don't need the `start.sh` and `screen.sh` files, and also you don't have to install Linux `screen`