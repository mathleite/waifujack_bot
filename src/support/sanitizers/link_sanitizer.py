from re import search


class LinkSanitizer:
    def __init__(self, link_list):
        self._sanitized_links = []
        self._retrieve_links_only(link_list)

    def _retrieve_links_only(self, links):
        for link in links:
            self._sanitized_links.append(
                search(r'(https?://)(\w*)(\S+[^"])', link).group()
            )

    @property
    def sanitized_links(self):
        return self._sanitized_links
