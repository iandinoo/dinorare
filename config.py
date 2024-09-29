#(©)NTMPRO




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6206993303:AAHOK1icY6TApVQXYWBvvW2hox3zb9w5b0w")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "6244159"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "3f15b21827506cb63890f756743be15f")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001893191083"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1494610306"))

#Port
PORT = os.environ.get("PORT", "8070")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://salomebase:salomebase@salome.3pfhf.mongodb.net/?retryWrites=true&w=majority&appName=Salome")
DB_NAME = os.environ.get("DATABASE_NAME", "Salome")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001720775575"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "ʜᴇʟʟᴏ {first}</b>\n\n<b>ᴀɴᴅᴀ ʜᴀʀᴜs ᴍᴇɴᴇᴋᴀɴ ʟɪɴᴋ ᴋᴏɴᴛᴇɴ ᴅᴀʀɪ ᴄʜᴀɴɴᴇʟ ᴛᴇʀsᴇʙᴜᴛ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋsᴇs ᴋᴏɴᴛᴇɴ.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6108349281 1494610306 1846991467 5015444972 7092423624 6440848191").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\nᴀɴᴅᴀ ᴅɪ ᴡᴀᴊɪʙ ᴋᴀɴ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋsᴇs ᴋᴏɴᴛᴇɴ ᴛᴇʀsᴇʙᴜᴛ</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌ᴋᴀᴍᴜ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ ʙɪᴛᴄʜ"

ADMINS.append(OWNER_ID)
ADMINS.append(1494610306)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
