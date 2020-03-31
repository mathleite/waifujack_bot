import configparser


class ConfigParser:
    def __init__(self, config_filename):
        self._config_parser = configparser.ConfigParser()
        self._config_parser.read(config_filename)

    def get_file_key_by_module(self, module, file_key):
        return self._config_parser.get(module, file_key)
