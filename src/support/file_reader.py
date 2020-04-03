import re


class FileReader:
    def __init__(self, fileName):
        self._file = open(fileName)
        self._matched_lines = []

    def read_file(self):
        file_content = self._file
        self._file.close()

        return file_content

    def find_text_key(self, text_key):
        file_content = self._file.readlines()

        for file_line in file_content:
            self._match_key_in_text_line(text_key, file_line)

        self._file.close()

        return self.retrieve_key_result(text_key)

    def _match_key_in_text_line(self, key, text_line):
        if key in text_line:
            self._matched_lines.append(text_line)

    def retrieve_key_result(self, text_key):
        found_key = re.search(f'[^{text_key}=].+', self._matched_lines[0])

        return found_key.group()
