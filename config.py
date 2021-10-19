# HuzunluArtemis

import os
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_USERNAME = os.environ.get('BOT_USERNAME','')
    if not BOT_USERNAME.startswith('@'): BOT_USERNAME = '@' + BOT_USERNAME # bu satıra dokunmayın.
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "HuzunluArtemis")
    OWNER_ID = int(os.environ.get('OWNER_ID', 0)) # give your owner id # if given 0 shell will not works
    AUTH_IDS = [int(x) for x in os.environ.get("AUTH_IDS", "0").split()] # if open to everyone give 0
    # forcesub vars
    FORCE_SUBSCRIBE_CHANNEL = os.environ.get('FORCE_SUBSCRIBE_CHANNEL','') # force subscribe channel link.
    if FORCE_SUBSCRIBE_CHANNEL == "" or FORCE_SUBSCRIBE_CHANNEL == " " or FORCE_SUBSCRIBE_CHANNEL == None: FORCE_SUBSCRIBE_CHANNEL = None # bu satıra dokunmayın.
    LOGGER.info(f"FORCE_SUBSCRIBE_CHANNEL: {FORCE_SUBSCRIBE_CHANNEL}") # debug
    # commands
    SHELL_COMMAND = os.environ.get('SHELL_COMMAND','shell')
    SHELL_COMMAND = [SHELL_COMMAND, SHELL_COMMAND+BOT_USERNAME] # bu satıra dokunmayın.
    HELP_COMMANDS = ["start", "help", "about", "yardım", "h", "y",
        f"start{BOT_USERNAME}", f"help{BOT_USERNAME}", f"about{BOT_USERNAME}",
        f"yardım{BOT_USERNAME}", f"h{BOT_USERNAME}", f"y{BOT_USERNAME}"]