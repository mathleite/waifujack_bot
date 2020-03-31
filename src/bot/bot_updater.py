from telegram.ext import Updater


class BotUpdater:
    def __init__(self, token):
        self._updater = Updater(
            token=token,
            use_context=True
        )

    @property
    def get(self):
        return self._updater
