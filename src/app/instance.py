from os import getenv
from dotenv import load_dotenv
from pyrogram import Client

if not load_dotenv():
    raise Exception('Unable to load .env file')
app: Client = Client(name=__name__,
                     api_id=getenv(key='API_KEY'),
                     api_hash=getenv(key='API_HASH'))