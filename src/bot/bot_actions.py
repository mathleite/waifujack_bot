class BotActions:
    def __init__(self, text):
        self._text = text

    def start(self, update, context):
        return context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=self._text
        )
