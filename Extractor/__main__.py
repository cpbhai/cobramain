import importlib
from pyrogram import Client
from Extractor.modules import ALL_MODULES
import os

# Get config from environment variables (set these in Heroku)
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Initialize the Pyrogram Client
app = Client(
    "main_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

# Import all modules dynamically
for all_module in ALL_MODULES:
    importlib.import_module("Extractor.modules." + all_module)

print("» ʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ ✨ 🎉")

if __name__ == "__main__":
    app.run()
