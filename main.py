from pyrogram import Client
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)

app = Client(
    "Pyrogram Bot",
    bot_token = "5192168337:AAGzHN3Yx8xcg8Ou5vDa830GejloyXKDtFc",
    api_id = 3024532,
    api_hash = "370817294c7a66e888fd06fa264f6dbd",
)

home_keyboard_pm = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Commands ❓", url=f"http://t.me/{BOT_USERNAME}?startgroup=new"
            ),
            InlineKeyboardButton(
                text="👤 Bot Owner",
                user_id = 1926090919,
            ),
        ],
        [
            InlineKeyboardButton(
                text="System Stats 🖥",
                url=f"http://t.me/{BOT_USERNAME}?startgroup=new",
            ),
            InlineKeyboardButton(
                text="🔎 Inline", switch_inline_query_current_chat = ''
            ),
        ],
        [
            InlineKeyboardButton(
                text="✚ Add Me To Your Group",
                url=f"http://t.me/{BOT_USERNAME}?startgroup=new",
            )
        ],
    ]
)

home_text_pm = (
    f"Hey there! My name is {BOT_NAME}. I can manage your "
    + "group with lots of useful features, feel free to "
    + "add me to your group."
)


@app.on_message(filters.command("start"))
async def start(client, message):
message.reply(
            home_text_pm,
            reply_markup=home_keyboard_pm,
        )



app.run()  # Automatically start() and idle()
