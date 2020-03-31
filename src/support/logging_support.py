import logging


class LoggingSupport:
    def __init__(self):
        self._configure_logging()

    def _configure_logging(self):
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )
