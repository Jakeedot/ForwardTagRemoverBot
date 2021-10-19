# HuzunluArtemis

from pyrogram import Client, filters
from HelperFunc.authUserCheck import AuthUserCheck
from HelperFunc.forceSubscribe import ForceSub
from HelperFunc.messageFunc import copyMessage, sendDocument, sendMessage
import logging

from config import Config
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)


@Client.on_message(filters.command(Config.LOG_COMMAND), group=1)
async def log(bot, message):
    if Config.OWNER_ID != 0 and message.from_user.id == Config.OWNER_ID:
        try:
            await sendDocument(message, 'log.txt')
        except Exception as e:
            await sendMessage(message, str(e))
            LOGGER.info(str(e))