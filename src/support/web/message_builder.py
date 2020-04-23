

class MessageBuilder:
    def __init__(self, links):
        self._message = ''
        self.build_link_message(links)

    def build_link_message(self, links):
        for link in links:
            self._message += f'{link} '

    @property
    def message(self):
        return self._message
