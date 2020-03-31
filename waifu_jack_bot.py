from telegram.ext import Updater, CommandHandler

from src.support.config_parser import ConfigParser
from src.support.logging_support import LoggingSupport

LoggingSupport()
config = ConfigParser('.waifujackrc')

updater = Updater(token=config.retrieve_app_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a bot, please talk to me!"
    )


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
