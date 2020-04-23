from src.support.file_reader import FileReader
from src.support.sanitizers.link_sanitizer import LinkSanitizer
from os import environ
import requests as req
import re


class WebSearch:
    def __init__(self):
        self._url = self._should_read_file('GOOGLE_IMAGE_URL')

    def search(self, item):
        response = req.get(self._url.replace(':replace', item))
        src_image = re.findall(r'(src="https?://\S+")', response.text)
        link_sanitizer = LinkSanitizer(src_image)

        return link_sanitizer.sanitized_links

    def _should_read_file(self, key_name):
        if key_name in environ:
            return environ[key_name]

        file = FileReader('.env')
        return file.find_text_key(key_name)
