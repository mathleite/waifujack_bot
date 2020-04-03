from src.fake.non_command_phrase import NonCommandPhrase


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
