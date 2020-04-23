

class LinkMessageBuilder:
    def __init__(self, links, links_length):
        self._message = 'I found these images for you: \n'
        self.build_link_message(links, links_length)

    def build_link_message(self, links, links_length):
        for index, link in enumerate(links[0:links_length]):
            self._message += f'- {index + 1}: {link} \n\n'

    @property
    def message(self):
        return self._message
