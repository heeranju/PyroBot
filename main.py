from pyrogram import Client, filter
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram.types import CallbackQuery
import randam
import os

PHOTO_LINK = [
 "Photo Link",
 "photo Link"
 ]

Op = Client(
    "Pyrogram Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
)


@Op.on_message(filters.command("start")) 
async def start_message(bot, message)
    button = [[
      InlineKeyboardButton("Mo Tech YT", callback_data="start",)
      ]]
    await messages.reply_photo(
        photo=random.choice(PHOTO_LINK),
        text="Hello {message.from_user.mention}   Bro Sugamano",
        reply_markup=InlineKeyboardMarkup(buttons)
    )



@Op.on_callback_query()
async def callback(bot, msg: CallbackQuery)
    if msg.data == "start":
        await message.message.edit(
            text=" hello {msg.from_user.mention}  Start Text"
        )



 Op.run()

