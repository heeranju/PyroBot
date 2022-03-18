from pyrogram import Client, filter
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram.types import CallbackQuery
import randam
import os

PHOTO_LINK = [
 "Photo Link",
 "photo Link"
 ]

app = Client(
    "Pyrogram Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
)


@app.on_inline_query()
def answer(client, inline_query):
    inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="Installation",
                input_message_content=InputTextMessageContent(
                    "Here's how to install **Pyrogram**"
                ),
                url="https://docs.pyrogram.org/intro/install",
                description="How to install Pyrogram",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "Open website",
                            url="https://docs.pyrogram.org/intro/install"
                        )]
                    ]
                )
            ),
            InlineQueryResultArticle(
                title="Usage",
                input_message_content=InputTextMessageContent(
                    "Here's how to use **Pyrogram**"
                ),
                url="https://docs.pyrogram.org/start/invoking",
                description="How to use Pyrogram",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "Open website",
                            url="https://docs.pyrogram.org/start/invoking"
                        )]
                    ]
                )
            )
        ],
        cache_time=1
    )


app.run()  # Automatically start()
