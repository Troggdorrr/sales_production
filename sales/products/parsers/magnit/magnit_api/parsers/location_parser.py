from functools import lru_cache
import json

from magnit_api.types import Location


class LocationParser:
    def __init__(self, raw_locations: str) -> None:
        self._raw_locations = self.__normalize_raw_locations(raw_locations)

    def __normalize_raw_locations(self, raw_locations: str) -> list[dict]:
        start = raw_locations.find("[")
        end = -1
        return json.loads(raw_locations[start:end])

    def parse(self) -> list[Location]:
        locations = []

        for raw_location in self._raw_locations:
            location = self._parse_location(raw_location)
            locations.append(location)

        return locations

    def _parse_location(self, raw_store: dict) -> Location:
        return Location(
            id=self._parse_id(raw_store),
            name=self._parse_name(raw_store),
        )

    def _parse_id(self, raw_location: dict) -> int:
        return raw_location["settlementId"]

    def _parse_name(self, raw_location: dict) -> str:
        return raw_location["name"]