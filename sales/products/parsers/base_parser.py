from django.core.files.images import ImageFile

from abc import abstractmethod, ABC

from products.models import Donor


class BaseParser(ABC):
    donor_name = None
    donor_url = None
    donor_logo = None

    def __init__(self) -> None:
        self.donor = self._save_donor()

    def _save_donor(self) -> Donor:
        with open(self.donor_logo, "rb") as logo:
            donor, is_created = Donor.objects.get_or_create(
                name=self.donor_name,
                url=self.donor_url,
                defaults={
                    "logo": ImageFile(logo),
                },
            )
        return donor

    @abstractmethod
    def save_data(self) -> None:
        pass