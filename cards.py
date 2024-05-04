from typing import Any


class Card:
    def __init__(self, suit, value, name) -> None:
        self.suit = suit
        self.value = value
        self.name = name
        
    def __str__(self) -> str:
        return f"{self.name} of {self.suit}"