from pyrogram import Client, filters, types
from sys import exit
from conf import env


api_id = env.int("API_ID")
api_hash = env.str("API_HASH")
session = env.str("SESSION") or None
src_chat = env.int("SOURCE") or None
dst_chat = env.int("DESTINATION") or None

bot = Client(session, api_id, api_hash)
media_group_ids = []

@bot.on_message(filters.chat(src_chat) & filters.media_group)
async def mg_handler(client, msg: types.Message) -> None:
    if msg.media_group_id not in media_group_ids:
        media_group_ids.append(msg.media_group_id)
        await bot.copy_media_group(dst_chat, src_chat, msg.message_id)

@bot.on_message(filters.chat(src_chat) & filters.media)
async def handler(client, msg: types.Message) -> None:
    await bot.copy_message(dst_chat, src_chat, msg.message_id)

if __name__ == "__main__":
    if session is None:
        print("\nPlease enter session name in .env file")
        exit(1)
    if (src_chat is None or dst_chat is None):
        print("\nPlease enter SOURCE and DESTINATION in .env file")
        exit(1)
    print("Bot is running.")
    bot.run()
