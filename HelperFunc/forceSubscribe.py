# https://raw.githubusercontent.com/viharasenindu/LexieTelegraphUploader/main/helpers/Forcesub.py
# HuzunluArtemis
# modified for this repo

import asyncio
from config import Config
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

async def ForceSub(bot: Client, event: Message):
    """
    Custom Pyrogram Based Telegram Bot's Force Subscribe Function by @viharasenindu.
    If User is not Joined Force Sub Channel Bot to Send a Message & ask him to Join First.
    
    :param bot: Pass Client.
    :param event: Pass Message.
    :return: It will return 200 if Successfully Got User in Force Sub Channel and 400 if Found that User Not Participant in Force Sub Channel or User is Kicked from Force Sub Channel it will return 400. Also it returns 200 if Unable to Find Channel.
    """
    if Config.FORCE_SUBSCRIBE_CHANNEL is not None:
        try:
            invite_link = await bot.create_chat_invite_link(
                chat_id=(
                    int(Config.FORCE_SUBSCRIBE_CHANNEL) if Config.FORCE_SUBSCRIBE_CHANNEL.startswith("-100") else Config.FORCE_SUBSCRIBE_CHANNEL
                ),
                member_limit = 1
            )
        except FloodWait as e:
            await asyncio.sleep(e.x)
            fix_ = await ForceSub(bot, event)
            return fix_
        except Exception as err:
            LOGGER.error(f"Error: {err}\nDo not forget to make admin your bot in forcesub channel.\nDestek / Support: {Config.CHANNEL_OR_CONTACT}") # debug
            return 200
        try:
            user = await bot.get_chat_member(chat_id=(int(Config.FORCE_SUBSCRIBE_CHANNEL) if Config.FORCE_SUBSCRIBE_CHANNEL.startswith("-100") else Config.FORCE_SUBSCRIBE_CHANNEL), user_id=event.from_user.id)
            if user.status == "kicked":
                await event.reply_text(
                    text=Config.YOU_ARE_BANNED_STR.format(Config.CHANNEL_OR_CONTACT),
                    parse_mode = 'html',
                    disable_notification=True,
                    disable_web_page_preview=True,
                    reply_to_message_id = event.message_id
                )
                return 400
            else:
                return 200
        except UserNotParticipant:
            await event.reply_text(
                text=Config.JOIN_CHANNEL_STR.format(event.from_user.mention),
                parse_mode = 'html',
                disable_notification=True,
                reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(f"{Config.JOIN_BUTTON_STR}", url=invite_link.invite_link)
                    ]
                ]
                ),
                disable_web_page_preview=True,
                reply_to_message_id = event.message_id
            )
            return 400
        except FloodWait as e:
            await asyncio.sleep(e.x)
            fix_ = await ForceSub(bot, event)
            return fix_
        except Exception as err:
            LOGGER.error(f"Error: {err}\nDo not forget to make admin your bot in forcesub channel.\nDestek / Support: {Config.CHANNEL_OR_CONTACT}") # debug
            return 200
    else:
        return 200