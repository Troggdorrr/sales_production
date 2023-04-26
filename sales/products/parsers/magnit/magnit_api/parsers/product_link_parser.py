from bs4 import BeautifulSoup, Tag

from functools import lru_cache

from magnit_api.utils import ProductHrefNormalizer
from magnit_api.types import ProductLink
from magnit_api.settings import BASE_URL


class ProductLinkParser:
    def __init__(self, raw_product_links: str):
        self._parser = BeautifulSoup(raw_product_links, "lxml")

    def parse(self) -> list[ProductLink]:
        links = []

        for raw_link in self._parser.find_all("a", {"class": "card-sale-new"}):
            link = self._parse_link(raw_link)
            links.append(link)

        return links

    def _parse_link(self, raw_link: Tag) -> str:
        return ProductLink(
            id=self._parse_id(raw_link),
            href=self._parse_href(raw_link)
        )

    def _parse_id(self, raw_link: Tag) -> int:
        normalizer = self.__get_link_normalizer(raw_link)
        return normalizer.get_id()

    def _parse_href(self, raw_link: Tag) -> str:
        normalizer = self.__get_link_normalizer(raw_link)
        return normalizer.get_href()

    @lru_cache
    def __get_link_normalizer(self, raw_link: Tag) -> ProductHrefNormalizer:
        link = BASE_URL + raw_link["href"]
        return ProductHrefNormalizer(link)