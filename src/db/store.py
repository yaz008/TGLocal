from db.db import with_cursor
from datetime import datetime
from sqlite3 import Cursor
from pyrogram.types import Message

@with_cursor
def store_message(cursor: Cursor, message: Message) -> None:
    cursor.execute('INSERT INTO messages VALUES (?, ?, ?, ?)',
                   (message.from_user.id,
                    message.chat.id,
                    datetime.now(),
                    bytes(message.text, encoding='UTF-8')))