from pyrogram import Client
from sys import exit
from config import env, logging


api_id = env.int("API_ID")
api_hash = env.str("API_HASH")
session = env.str("SESSION") or None
src_chats = env.list("SOURCE") or None
dst_chat = env.int("DESTINATION") or None

bot = Client(session, api_id, api_hash)

async def copy_chat(chat_id) -> None:
    media_group_ids = list()
    count = await bot.get_history_count(chat_id)
    offset = 0
    while count > 0:
        messages = await bot.get_history(chat_id, offset=offset, reverse=True)
        for msg in messages:
            if msg.text:
                await bot.copy_message(dst_chat, chat_id, msg.message_id)
                logging.warning("Copied text message from {}".format(msg.chat.title))
            elif not msg.media_group_id:
                await bot.copy_message(dst_chat, chat_id, msg.message_id)
                logging.warning("Copied media message from {}".format(msg.chat.title))
            elif msg.media_group_id not in media_group_ids:
                media_group_ids.append(msg.media_group_id)
                await bot.copy_media_group(dst_chat, chat_id, msg.message_id)
                logging.warning("Copied media group message from {}".format(msg.chat.title))
            else:
                continue
        count -= 100
        offset += 100
    

if __name__ == "__main__":
    if session is None:
        print("\nPlease enter session name in .env file")
        exit(1)
    if (src_chats is None or dst_chat is None):
        print("\nPlease enter SOURCE and DESTINATION in .env file")
        exit(1)
    logging.warn("Bot is starting...")
    for src_chat in map(int, src_chats):
        bot.connect()
        print("{} copying,,.".format(bot.get_chat(src_chat).title))
        bot.run(copy_chat(src_chat))
    print("Chat copying was finished successfully.")
    
