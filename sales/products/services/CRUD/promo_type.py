from products.models import PromoType


class PromoTypeCRUD:
    @staticmethod
    def get_list():
        return PromoType.objects.all()
