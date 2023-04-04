class Kommun: 
    def __init__(self, namn: str, id: str, data: dict[str: dict[str: int]]) -> None:
        self.namn = namn
        self.id = id
        self.data = data

    def __str__(self) -> str:
        return f"Kommunen {self.namn} har id {self.id} och har som senast totalt {self.data['2023M01']['total']} människor som bodde i kommunen. "