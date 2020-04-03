from telegram.ext import CommandHandler, MessageHandler, Filters
from src.bot.bot_actions import BotActions
from src.bot.bot_updater import BotUpdater
from src.support.file_reader import FileReader
from src.support.logger import Logger

Logger()
file = FileReader('.env')

updater = BotUpdater(token=file.find_text_key('BOT_KEY'))

updater = updater.get

dispatcher = updater.dispatcher

actions = BotActions(text='I\'m a bot, please talk to me!')

start_handler = CommandHandler('start', actions.start)

echo_handler = MessageHandler(Filters.text, actions.retrieve_non_command_phrase)
dispatcher.add_handler(start_handler)

updater.start_polling()
