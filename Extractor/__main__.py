import asyncio
import importlib
import signal
from pyrogram import Client
from Extractor.modules import ALL_MODULES

loop = asyncio.get_event_loop()
shutdown_event = asyncio.Event()

async def sumit_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("Extractor.modules." + all_module)

    print("» ʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ ✨ 🎉")

    # Wait until shutdown_event is set
    await shutdown_event.wait()

    print("» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")

def handle_sigterm():
    shutdown_event.set()  # Triggers the wait to finish
    for task in asyncio.all_tasks():
        task.cancel()

if __name__ == "__main__":
    signal.signal(signal.SIGTERM, lambda s, f: handle_sigterm())

    try:
        loop.run_until_complete(sumit_boot())
    except asyncio.CancelledError:
        pass
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
