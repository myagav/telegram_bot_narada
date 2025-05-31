from typing import Literal
from dataclasses import dataclass

TextT = Literal["quote", "joke"]


@dataclass
class Text:
    id: int
    text: str
    type: TextT
