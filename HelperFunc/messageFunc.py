import asyncio
from pyrogram.errors.exceptions.bad_request_400 import MessageNotModified
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

async def sendMessage(toReplyMessage: Message, replyText: str, replyButtons:InlineKeyboardMarkup = None):
    try:
        return await toReplyMessage.reply_text(replyText,
            disable_web_page_preview=True,
            parse_mode='markdown',
            quote=True,
            reply_markup = replyButtons)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await sendMessage(toReplyMessage)
    except Exception as e:
        LOGGER.info(str(e))

async def editMessage(toEditMessage: Message, editText: str, replyButtons:InlineKeyboardMarkup = None):
    try:
        return await toEditMessage.edit(text=editText,
            disable_web_page_preview=True,
            parse_mode='markdown',
            reply_markup = replyButtons)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await editMessage(toEditMessage)
    except MessageNotModified as e:
        LOGGER.info(str(e))
    except Exception as e:
        LOGGER.info(str(e))

async def copyMessage(toReplyDocument: Message):
    try:
        return await toReplyDocument.copy(chat_id=toReplyDocument.from_user.id)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await copyMessage(toReplyDocument)
    except Exception as e:
        LOGGER.info(str(e))