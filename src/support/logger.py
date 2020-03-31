import logging


class Logger:
    def __init__(self):
        self._configure_logger()

    def _configure_logger(self):
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )
