from urllib.parse import urlparse, urljoin

from magnit_api.settings import BASE_URL


class ProductHrefNormalizer:
    def __init__(self, raw_link: str) -> None:
        self._raw_link = raw_link

    def get_id(self) -> int:
        return int("".join([char for char in self.get_href() if char.isdigit()]))
    
    def get_href(self) -> str:
        return urljoin(self._raw_link, urlparse(self._raw_link).path)