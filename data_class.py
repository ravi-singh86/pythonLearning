#Python3.7 only
from dataclasses import dataclass

@dataclass
class PlayingCard:
    rank: str
    suit: str
