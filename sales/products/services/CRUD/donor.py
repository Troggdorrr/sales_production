from products.models import Donor


class DonorCRUD:
    @staticmethod
    def get_list():
        return Donor.objects.all()
