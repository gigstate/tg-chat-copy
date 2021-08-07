# Telegram Copy Bot


## What it does
This bot can copy messages from a chats or channels your choose to another chat (simple user, channel, etc)

## How to use
1. Copy `.env.example` to `.env`.
    ```
    cp .env.example .env
    ```
2. Obtain `api_id` and `api_hash` from [this link](https://my.telegram.org/apps) and fill it inside Telegram Configuration section of `.env` alongside other configurations (such as phone number of your user which acts as your bot)
3. Run it and login to telegram (may take some minutes to build image for the first time):
   ```
   sudo docker-compose run bot
   ```
4. Without docker running:
   ```
   python3 -m pip install -r requirements.txt
   python3 -u app/main.py
   ```

