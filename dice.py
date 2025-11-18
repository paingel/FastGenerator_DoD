# dice.py
import random


def roll_dice(n: int, sides: int) -> list[int]:
    """Slå n stycken tärningar med 'sides' sidor och returnera en lista med resultaten."""
    return [random.randint(1, sides) for _ in range(n)]


def roll_4d6_drop_lowest() -> int:
    """Slå 4T6, ta bort den lägsta, summera resten (standard i DoD 23)."""
    rolls = roll_dice(4, 6)
    rolls.sort()
    return sum(rolls[1:])  # släng lägsta
