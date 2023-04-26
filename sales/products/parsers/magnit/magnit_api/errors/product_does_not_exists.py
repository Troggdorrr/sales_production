class ProductDoesNotExists(Exception):
    def __init__(self, id: int) -> None:
        self.id = id
    
    def __str__(self) -> str:
        return f"Product with id {self.id} does not exists"