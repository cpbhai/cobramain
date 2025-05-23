from pyrogram import Client
import os

API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

if __name__ == "__main__":
    app = Client("test", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
    app.run()
