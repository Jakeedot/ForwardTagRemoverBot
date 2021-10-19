# HuzunluArtemis

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
        LOGGER.info(str(e))
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
        LOGGER.info(str(e))
        await editMessage(toEditMessage)
    except MessageNotModified as e:
        LOGGER.info(str(e))
    except Exception as e:
        LOGGER.info(str(e))

async def copyMessage(toReplyDocument: Message, toCopyChatId: int = None, sendAsReply: bool = False):
    if toCopyChatId is None: toCopyChatId = toReplyDocument.chat.id
    try:
        if sendAsReply:
            return await toReplyDocument.copy(chat_id=toCopyChatId,
                reply_to_message_id=toReplyDocument.message_id)
        else:
            return await toReplyDocument.copy(chat_id=toCopyChatId)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        LOGGER.info(str(e))
        await copyMessage(toReplyDocument)
    except Exception as e:
        LOGGER.info(str(e))

async def sendDocument(toReplyDocument: Message, filePath: str):
    try:
        return await toReplyDocument.reply_document(filePath)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        LOGGER.info(str(e))
        await sendDocument(toReplyDocument)
    except Exception as e:
        LOGGER.info(str(e))