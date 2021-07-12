import telethon
from telethon import TelegramClient
import asyncio
api = "1833219373:AAH-JqUzAcR0473AjIwO-J1sDwGCvrXw3ds"
client = TelegramClient("session","2181594","5d5323c00506b2e42d429a0ca3904952")
client.start(bot_token=api)

async def massege():
    await client.send_file("@jokerrap2","main.py")
asyncio.get_event_loop().run_until_complete(massege())