# Telegram Copy Bot


## What it does
`copier.py` - This script can copy all message history from a chats or channels your choose to another chat (simple user, channel, etc)

`handler.py` - This script can copy new messages from a chats or channels your choose to another chat (simple user, channel, etc)

`downloader.py` - This script can download all medias from a chats or channels your choose to another chat (simple user, channel, etc)
## How to use
1. Copy `.env.example` to `.env`.
    ```
    cp .env.example .env
    ```
2. Obtain `api_id` and `api_hash` from [this link](https://my.telegram.org/apps) and fill it inside Telegram Configuration section of `.env` alongside other configurations (such as phone number of your user which acts as your bot)
   ```
4. How to run:
   ```
   python3 -m pip install -r requirements.txt
   python3 app/copier.py
   python3 app/handler.py
   python3 app/downloader.py
   ```

