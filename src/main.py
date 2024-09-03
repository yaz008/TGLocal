from app import app
from pyrogram.client import Client
from pyrogram.types import Message

@app.on_message(filters=None)
def on_message(_: Client, message: Message) -> None:
    print(message.text)

if __name__ == '__main__':
    app.run()