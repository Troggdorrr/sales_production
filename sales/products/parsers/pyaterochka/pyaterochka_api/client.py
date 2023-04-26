from .methods import GetProducts, IterProducts, GetStores, IterStores


class Client(GetProducts, IterProducts, GetStores, IterStores):
    ...
