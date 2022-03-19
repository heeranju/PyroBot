from pyrogram import Client, filters
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)

app = Client(
    "Pyrogram Bot",
    bot_token = "5192168337:AAGzHN3Yx8xcg8Ou5vDa830GejloyXKDtFc",
    api_id = 3024532,
    api_hash = "370817294c7a66e888fd06fa264f6dbd",
)



@app.on_message(filters.text & filters.private)
def echo(client, message):
    message.reply(message.text)



app.run()  # Automatically start() and idle()
