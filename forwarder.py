# HuzunluArtemis

import logging
import os
from config import Config
import pyrogram
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

if __name__ == '__main__':
    #
    plugins = dict(root = 'plugins')
    #
    app = pyrogram.Client("AnonymousMessageForwarderBot",
		bot_token = Config.BOT_TOKEN,
		api_id = Config.APP_ID,
		api_hash = Config.API_HASH,
		plugins = plugins)
    #
    app.start()
    #
    LOGGER.info(msg="App Started.")
    #
    pyrogram.idle()
    #
    LOGGER.info(msg="App Stopped.")