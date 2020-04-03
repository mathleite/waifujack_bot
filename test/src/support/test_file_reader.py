from unittest import TestCase
from unittest_data_provider import data_provider
from src.support.file_reader import FileReader


class TestFileReader(TestCase):
    _provideNonExistentFiles = lambda: [
        ['./wrong/path/file'],
        ['../../../.non-exist'],
        ['/var/www/.env'],
        ['..env'],
        ['requirements.yml'],
    ]

    @data_provider(_provideNonExistentFiles)
    def test_ConfigParserInstance_ShouldThrowException_WhenGivenANonExistentFile(self, files):
        with self.assertRaises(Exception):
            FileReader(files)
