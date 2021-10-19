# HuzunluArtemis

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from pyrogram.types.messages_and_media.message import Message
from HelperFunc.authUserCheck import AuthUserCheck
from HelperFunc.messageFunc import sendMessage
from HelperFunc.forceSubscribe import ForceSub
from config import Config
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)


@Client.on_message(filters.command(Config.HELP_COMMANDS), group=1)
async def help(client, message: Message):
	# return
	if not await AuthUserCheck(message.chat.id, message.from_user.id): return
	if await ForceSub(client, message) == 400: return
	# do
	tumad = message.from_user.first_name
	if message.from_user.last_name != None: tumad += f" {message.from_user.last_name}"
	toSendStr = f"Esenlikler / Hi {tumad}" + \
	f"\n\n🇹🇷 Ben basit bir yönlendirici botuyum."+ \
	f"\nGönderdiğiniz her mesajı anonimleştiririm." + \
	f"\nBenim göndereceğim mesajı gönderirsiniz."+ \
	f"\nBöylece mesajı sizin gönderdiğiniz belli olmaz."+ \
	f"\nNeyi bekliyorsun? Bana birşey yaz ve dene!"+ \
	f"\n\n🇬🇧 This a simple forwarder bot."+ \
	f"\nI anonymize every message you send"+ \
	f"\nYou send the message I sent."+ \
	f"\nThus, it is not clear that you sent the message."+ \
	f"\nWhat are you waiting for? Write something to me and try it!"
	reply_markup = None
	if Config.UPDATES_CHANNEL != None and Config.UPDATES_CHANNEL != "" and Config.UPDATES_CHANNEL != " ":
		reply_markup=InlineKeyboardMarkup(
			[
				[InlineKeyboardButton(
				text = "🔥 Güncellemeler / Updates",
				url = "https://t.me/" + Config.UPDATES_CHANNEL)
				]
			])
	await sendMessage(message,toSendStr,reply_markup)
    
