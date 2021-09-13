# HuzunluArtemis

import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "HuzunluArtemis")
