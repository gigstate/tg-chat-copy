from telethon import TelegramClient, events, types
from sys import exit
from env import env

api_id = env.int("API_ID")
api_hash = env.str("API_HASH")
session = env.str("SESSION")
src_chat = env.int("SOURCE") or None
dst_chat = env.int("DESTINATION") or None

client = TelegramClient(session, api_id, api_hash)

@client.on(events.NewMessage(chats=src_chat, outgoing=False))
async def handler(event: types.Message) -> None:
    if not event.media:
        return
    await copy_message(event)

async def copy_message(event: types.Message) -> None:
    await client.send_message(dst_chat, event.message)

if __name__ == "__main__":
    if session is None:
        print("\nPlease enter session name in .env file")
        exit(1)
    if (src_chat is None or dst_chat is None):
        print("\nPlease enter SOURCE and DESTINATION in .env file")
        exit(1)
    client.start()
    print("Bot is running.")
    client.run_until_disconnected()
