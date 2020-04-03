from telegram.ext import CommandHandler, MessageHandler, Filters
from src.bot.bot_actions import BotActions
from src.bot.bot_updater import BotUpdater
# from src.support.file_reader import FileReader
from src.support.logger import Logger
from os import environ

Logger()
# file = FileReader('.env')

updater = BotUpdater(token=environ['BOT_KEY'])

updater = updater.get

dispatcher = updater.dispatcher

actions = BotActions(text='I\'m a bot, please talk to me!')

start_handler = CommandHandler('start', actions.start)

echo_handler = MessageHandler(Filters.text, actions.retrieve_non_command_phrase)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)

updater.start_polling()
