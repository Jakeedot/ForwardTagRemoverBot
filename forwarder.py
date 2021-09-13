# HuzunluArtemis

from pyrogram import Client, filters
import pyrogram
from pyrogram.types import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from pyrogram.types.messages_and_media.message import Message
from config import Config

app = Client(
	"AnonymousMessageForwarderBot",
	api_id=Config.APP_ID,
	api_hash=Config.API_HASH,
	bot_token=Config.BOT_TOKEN
)

app.start()
print("Bot Started!")

@app.on_message(filters.command(["start", "help", "about", "yardım", "h", "y"]))
async def helps(client, message: Message):
	tumad = message.from_user.first_name
	if message.from_user.last_name != None:
		tumad += f" {message.from_user.last_name}"
	if Config.UPDATES_CHANNEL is not None and Config.UPDATES_CHANNEL is not "" and Config.UPDATES_CHANNEL is not " ":
		channel = "https://t.me/" + Config.UPDATES_CHANNEL
		reply_markup=InlineKeyboardMarkup(
			[
				[InlineKeyboardButton(
				text = "🔥 Güncellemeler / Updates",
				url = channel)
				]
			])
	else:
		reply_markup=None
	await message.reply_text(text=
		f"Esenlikler / Hi {tumad}"
		f"\n\n🇹🇷 Ben basit bir yönlendirici botuyum."
		f"\nGönderdiğiniz her mesajı anonimleştiririm."
		f"\nBenim göndereceğim mesajı gönderirsiniz."
		f"\nBöylece mesajı sizin gönderdiğiniz belli olmaz."
		f"\nNeyi bekliyorsun? Bana birşey yaz ve dene!"
		f"\n\n🇬🇧 This a simple forwarder bot."
		f"\nI anonymize every message you send"
		f"\nYou send the message I sent."
		f"\nThus, it is not clear that you sent the message."
		f"\nWhat are you waiting for? Write something to me and try it!",
		reply_markup=reply_markup,
		disable_web_page_preview=True,
		parse_mode="md"
		)

@app.on_message(filters.all, group=2)
async def forward(client, message):
    await message.copy(chat_id=message.from_user.id)
	
pyrogram.idle()
app.stop()
print("Bot Stopped!")
