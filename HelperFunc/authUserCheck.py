# HuzunluArtemis

from config import Config

async def AuthUserCheck(chat_id, user_id):
    if 0 in Config.AUTH_IDS:
        return True
    elif user_id in Config.AUTH_IDS:
        return True
    elif chat_id in Config.AUTH_IDS:
        return True
    else:
        return False
