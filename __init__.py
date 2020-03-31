from telegram.ext import CommandHandler
from src.bot.bot_actions import BotActions
from src.bot.bot_updater import BotUpdater
from src.support.config_parser import ConfigParser
from src.support.logger import Logger

Logger()
config = ConfigParser('.env')

updater = BotUpdater(
    token=config.get_file_key_by_module('TELEGRAM', 'BOT_KEY'),
)

updater = updater.get

dispatcher = updater.dispatcher

actions = BotActions(text='I\'m a bot, please talk to me!')

start_handler = CommandHandler('start', actions.start)
dispatcher.add_handler(start_handler)

updater.start_polling()
