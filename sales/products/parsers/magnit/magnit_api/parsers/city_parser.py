from magnit_api.types import City


class CityParser:
    def __init__(self, raw_cities: dict) -> None:
        self.raw_cities = raw_cities

    def get_cities(self) -> list[City]:
        cities = []

        for raw_city in self.raw_cities:
            cities.append(self._get_city(raw_city))

        return cities

    def _get_city(self, raw_city: dict) -> City:
        return City(
            id=raw_city["id"],
            name=raw_city["city"],
        )
