import configparser


class ConfigParser:
    def __init__(self, config_filename):
        config_parser = configparser.ConfigParser()
        config_parser.read(config_filename)
        self._token = config_parser.get('TELEGRAM', 'WAIFUJACK_BOT_KEY')

    @property
    def retrieve_app_token(self):
        return self._token
