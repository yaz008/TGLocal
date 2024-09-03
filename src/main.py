from app import app
from pyrogram.client import Client
from pyrogram.types import Message
from db import store_message

@app.on_message(filters=None)
def on_message(_: Client, message: Message) -> None:
    store_message(message)

if __name__ == '__main__':
    app.run()