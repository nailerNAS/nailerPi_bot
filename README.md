# nailerPi_bot

# Linux requirements:
  * wakeonlan
  * python3
  * pip3 (Optional, needed for easy installation of pyTelegramBotAPI lib)
  * screen (Optional, needed for screen.sh script to work; recommended anyways)
  
  Raspbian/Ubuntu/Debian derivatives:
    sudo apt update && sudo apt install python3 wakeonlan python3-pip screen -y

# Python requirements:
  * pyTelegramBotAPI
  
  If you have pip3 installed (python3-pip):
    pip3 install --user pytelegrambotapi <--Recommended
    or
    sudo pip3 install pytelegrambotapi <--Installs the lib system-wide

# config.py
  Modify this file with **your own** Bot Token [@BotFather](https://telegram.me/botfather)
  Use **your** Telegram account ID [@getidsbot](https://telegram.me/getidsbot)
  Use **your own** MAC address and interface names (on Raspbian you don't need to change interface names)
  
  Additionally you can change buttons text in main.py at the beginning

# Startup
  There are two scripts: start.sh and screen.sh
  * start.sh launches the bot and restarts it in case if bot stops for any reason (like unhandled exception)
  * screen.sh simply launches start.sh in the background by using Linux screen. You can reattach to that background console session by running ```screen -r nailerpi```. The ```nailerpi``` name of screen can be modified in screen.sh
  
  To make your bot start automatically on boot, run ```crontab -e``` and add this to last line:
    ```@reboot sh /home/pi/nailerpi/screen.sh >/dev/null 2>&1```
    where */home/pi/nailerpi* is path to your bot
