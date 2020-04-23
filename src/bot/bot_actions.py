from src.fake.non_command_phrase import NonCommandPhrase
from src.bot.web.web_search import WebSearch
from src.support.web.link.link_message_builder import LinkMessageBuilder
from src.support.web.message_builder import MessageBuilder


class BotActions:
    def __init__(self, text):
        self._text = text

    def start(self, update, context):
        return context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=self._text
        )

    def retrieve_non_command_phrase(self, update, context):
        return context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=NonCommandPhrase().retrieve_random_phrase()
        )

    def search_web_result(self, update, context):
        web_search = WebSearch()
        arguments = MessageBuilder(context.args)
        builder = LinkMessageBuilder(web_search.search(arguments.message), 4)

        return context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=builder.message
        )
