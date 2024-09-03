from sqlite3 import connect, Cursor
from typing import Callable
from pyrogram.types import Message
from os import getenv

CREATE_QUERY: str = """CREATE TABLE IF NOT EXISTS messages (
    user_id INTEGER NOT NULL,
    chat_id INTEGER NOT NULL,
    datetime DATETIME,
    text BLOB
)
"""

def with_cursor(func: Callable[[Cursor, Message], None]) -> Callable[[Message], None]:
    with connect(database=getenv(key='DB_PATH')) as connection:
        cursor: Cursor = connection.cursor()
        cursor.execute(CREATE_QUERY)
    def wrapper(message: Message) -> None:
        with connect(database=getenv(key='DB_PATH')) as connection:
            cursor: Cursor = connection.cursor()
            func(cursor, message)
    return wrapper