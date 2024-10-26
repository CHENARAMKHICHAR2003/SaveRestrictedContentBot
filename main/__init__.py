#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("24894984", default=None, cast=int)
API_HASH = config("4956e23833905463efb588eb806f9804", default=None)
BOT_TOKEN = config("7601293855:AAG0J1lG04wfEnK9J1GnImfOWN7X_2wyaS4", default=None)
SESSION = config("BQDNvmIAZ1X9L23p3vjYqYYF0XbpE1q0KPK8kFX2kY-GLwn91_F3zAGQR0vR-HHOpNr4qIT2njA0ayI9VelAz2X1JbDfaIi-i5oVECqa1mn6FFQ_bnVIoSWxGNOUcMIbFV-sVkGaKqIYhA61-L1ZYb5jjk5IXFAWQQP-WxXNXnh6Pwdhrahvt42J-boZsIvYnVkjnrc8_RvvNoaRWrXoxXzRHHEyvtTMWKnQHZ2EUzZ8twEBeZ0_cUJf6g7cQxWbKYO1xTqcmFPd9vD0le-zKEY6FG9K84D2LZOMn560Ex3BletkE2nIMcA23N4hD6p4PXHw_XoN-F1S2ZGBPhz8ok5Fs4HlzQAAAAA1y9g-AA", default=None)
FORCESUB = config("-1002182291545", default=None)
AUTH = config("902551614", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
