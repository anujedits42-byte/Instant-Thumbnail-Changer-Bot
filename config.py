# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat
import os
import random
# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat
# Bot Configuration
API_TOKEN = os.environ.get("API_TOKEN", "7820299629:AAGs1AKd-IJZFi7I6K4Yoo5Yps8i-FiUphg")
# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat
# MongoDB
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://Anujedit:Anujedit@cluster0.7cs2nhd.mongodb.net/?appName=Cluster0")
DB_NAME = "Anujedit"
# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat
# Owner/Admin
OWNER_ID = int(os.environ.get("OWNER_ID", "7892805795"))
# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat
# UI URLs - Multiple images that rotate randomly
# Use DIRECT image URLs (https://i.ibb.co/...) not page URLs (https://ibb.co/...)
START_PICS = [
    "https://image.zaw-myo.workers.dev/image/571cab4b-d85c-4bfc-b1ad-14a8e99633ee",
    # Add more direct image URLs here
]
# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat
CHANNEL_URL = os.environ.get("CHANNEL_URL", "https://t.me/log_channel_a")
DEV_URL = os.environ.get("DEV_URL", "https://t.me/anujedits76")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003515041061"))  # e.g., -100xxxxxxxxxxxx
# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat

def get_random_pic() -> str:
    """Get a random image from START_PICS."""
    if START_PICS:
        return random.choice(START_PICS)
    return None
# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat

