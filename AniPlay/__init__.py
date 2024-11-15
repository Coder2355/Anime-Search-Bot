import os
from pyrogram.client import Client

app = Client(
    "AniPlay",
    api_id= int(os.environ.get("APP_ID", "21740783")),
    api_hash= os.environ.get("API_HASH", "a5dc7fec8302615f5b441ec5e238cd46"),
    bot_token= os.environ.get("TOKEN", "7444872585:AAHYzPX_gygFh9xYvu0-k7YOUg7BSG_hzHg")
)
