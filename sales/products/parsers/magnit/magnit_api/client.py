from .requests import GetShopsRequest, GetCitiesRequest, GetProductsRequest
from .parsers import CityParser, ProductParser, ShopParser
from .types import City, Product, Shop


class Client:
    def get_cities(self) -> list[City]:
        request = GetCitiesRequest()
        response = request.get_cities()
        parser = CityParser(response.json()["cities"])
        return parser.get_cities()

    def get_shops(self, city: City) -> list[Shop]:
        request = GetShopsRequest(city)
        response = request.get_shops()
        parser = ShopParser(response.json()["stores"])
        return parser.get_shops()
    
    def get_products(self, shop: Shop) -> list[Product]:
        request = GetProductsRequest(shop)
        response = request.get_products()
        parser = ProductParser(response.json()["data"])
        return parser.get_products()