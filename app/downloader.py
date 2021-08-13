from pyrogram import Client
from sys import exit
from config import env, logging
from datetime import datetime
import os

api_id = env.int("API_ID")
api_hash = env.str("API_HASH")
session = env.str("SESSION") or None
src_chats = env.list("SOURCE") or None
dst_chat = env.int("DESTINATION") or None

bot = Client(session, api_id, api_hash)

def rename(file_path: str, folder: str, num: int = None) -> None:
    new_fp, ext = file_path.rsplit('.', 1)
    num = f"_{num}" if num else ""
    ap, fp = new_fp.rsplit('/', 1)
    new_fp = ap + f"/{folder}/" + fp
    new_fp = "".join(new_fp.rsplit('_', 1)[0]) + f"{num}.{ext}"
    try:
        os.mkdir(f"./app/downloads/{folder}/")
    except FileExistsError:
        pass
    os.rename(file_path, new_fp)


async def copy_chat(chat_id: int, folder: str) -> None:
    available_media = ("audio", "document", "photo", "sticker", "animation", "video", "voice", "video_note",
                           "new_chat_photo")
    count = await bot.get_history_count(chat_id)
    offset = 0
    while count > 0:
        messages = await bot.get_history(chat_id, offset=offset, reverse=True)
        media_group_id = 0
        progress = 0
        num = 1
        for msg in messages:
            progress += 1
            for kind in available_media:
                media  = getattr(msg, kind, None)
                if media is not None:
                    break
            else:
                logging.warning("[{}/{}] Skipped non-media message from {}".format(progress, count, msg.chat.title))
                continue  
            media = msg.media or "media"
            if msg.media_group_id:
                if msg.media_group_id == media_group_id:
                    num += 1
                else:
                    media_group_id = msg.media_group_id
                    num = 1
                fp = await msg.download()
                rename(fp, folder, num)
                logging.warning("[{}/{}] Downloaded {} ({}) from {}".format(progress, count, media, num, msg.chat.title))
            else:
                fp = await msg.download()
                rename(fp, folder)
                logging.warning("[{}/{}] Downloaded {} from {}".format(progress, count, media, msg.chat.title))
        count -= 100
        offset += 100
    

if __name__ == "__main__":
    if session is None:
        print("\nPlease enter session name in .env file")
        exit(1)
    if (src_chats is None or dst_chat is None):
        print("\nPlease enter SOURCE and DESTINATION in .env file")
        exit(1)
    print("Bot is starting...")
    for src_chat in map(int, src_chats):
        bot.connect()
        print("{} Downloading,,.".format(folder := bot.get_chat(src_chat).title))
        bot.run(copy_chat(src_chat, folder))
    print("Chats downloading was finished successfully.")
    
