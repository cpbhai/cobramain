import asyncio
import importlib
import signal
import sys
from pyrogram import idle
from Extractor.modules import ALL_MODULES

loop = asyncio.get_event_loop()

# Graceful shutdown handler
def shutdown_handler(signum, frame):
    print("» Shutdown signal received. Exiting...")
    sys.exit(0)

# Register signals
signal.signal(signal.SIGTERM, shutdown_handler)
signal.signal(signal.SIGINT, shutdown_handler)

async def sumit_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("Extractor.modules." + all_module)

    print("» ʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ ✨ 🎉")
    await idle()
    print("» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")

if __name__ == "__main__":
    loop.run_until_complete(sumit_boot())
