from pyrogram.handlers import MessageHandler
from pyrogram import Client, filters, types
from sys import exit
from conf import env


api_id = env.int("API_ID")
api_hash = env.str("API_HASH")
session = env.str("SESSION") or None
src_chats = env.list("SOURCE") or None
dst_chat = env.int("DESTINATION") or None

bot = Client(session, api_id, api_hash)
media_group_ids = []

async def mg_handler(client, msg: types.Message) -> None:
    if msg.media_group_id not in media_group_ids:
        media_group_ids.append(msg.media_group_id)
        await bot.copy_media_group(dst_chat, msg.chat.id, msg.message_id)

async def handler(client, msg: types.Message) -> None:
    await bot.copy_message(dst_chat, msg.chat.id, msg.message_id)

if __name__ == "__main__":
    if session is None:
        print("\nPlease enter session name in .env file")
        exit(1)
    if (src_chats is None or dst_chat is None):
        print("\nPlease enter SOURCE and DESTINATION in .env file")
        exit(1)
    print("Bot is starting.")
    for i, src_chat in enumerate(src_chats, 1):
        src_chat = int(src_chat)
        print(src_chat, "handler added.")
        bot.add_handler(MessageHandler(mg_handler, filters.chat(src_chat) & filters.media_group))
        bot.add_handler(MessageHandler(handler, filters.chat(src_chat) & filters.media))
    print("Handlers setup was finished successfully.")
    bot.run()
