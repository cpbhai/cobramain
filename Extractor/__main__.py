import asyncio
import importlib
import signal
from pyrogram import idle
from Extractor.modules import ALL_MODULES

loop = asyncio.get_event_loop()

async def sumit_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("Extractor.modules." + all_module)

    print("» ʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ ✨ 🎉")

    # Wait until the bot is stopped manually or SIGTERM is caught
    await idle()

    print("» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")


def handle_sigterm():
    """Cancel all running tasks to exit cleanly."""
    for task in asyncio.all_tasks(loop):
        task.cancel()


if __name__ == "__main__":
    # Register SIGTERM handler for graceful shutdown
    signal.signal(signal.SIGTERM, lambda s, f: handle_sigterm())

    try:
        loop.run_until_complete(sumit_boot())
    except asyncio.CancelledError:
        pass
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
