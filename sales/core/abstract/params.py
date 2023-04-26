from rest_framework.exceptions import ValidationError

from abc import abstractmethod, ABC


class Params(ABC):
    @abstractmethod
    def validate(self) -> None:
        pass

    def _raise_errors(self, errors: dict):
        errors = self.__normalize_errors(errors)

        if errors:
            raise ValidationError(errors)

    def __normalize_errors(self, errors: dict) -> dict:
        normalized_errors = {}

        for key, value in errors.items():
            if value:
                normalized_errors[key] = value

        return normalized_errors