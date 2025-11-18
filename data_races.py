# data_races.py
from dataclasses import dataclass
from typing import Optional


@dataclass
class Race:
    name: str
    base_move: int
    ability_name: str  # bara namnet på släktesförmågan
    example_names: list[str]


RACES: dict[str, Race] = {
    "Människa": Race(
        name="Människa",
        base_move=10,
        ability_name="Anpasslig",
        example_names=["Joruna", "Tym", "Halvelda", "Garmander", "Verolun", "Lothar"],
    ),
    "Halvling": Race(
        name="Halvling",
        base_move=8,
        ability_name="Svårfångad",
        example_names=["Belma", "Filbo", "Dinla", "Humble", "Nedrin", "Tilda"],
    ),
    "Dvärg": Race(
        name="Dvärg",
        base_move=8,
        ability_name="Långsint",
        example_names=["Borin", "Grem", "Hildra", "Kargun", "Mardin", "Una"],
    ),
    "Alv": Race(
        name="Alv",
        base_move=10,
        ability_name="Inre frid",
        example_names=["Elion", "Lyra", "Fenn", "Naela", "Sarian", "Thalan"],
    ),
    "Anka": Race(
        name="Anka",
        base_move=8,
        ability_name="Vresig / Simfötter",
        example_names=["Kvack", "Sörl", "Tusenfjäder", "Vargöga", "Raspen", "Dunvinge"],
    ),
    "Vargfolk": Race(
        name="Vargfolk",
        base_move=12,
        ability_name="Jaktsinne",
        example_names=["Wyld", "Vargskugga", "Lunariem", "Obdurian", "Frostbite", "Wuldenhall"],
    ),
}


def roll_random_race(t12: int) -> Race:
    """
    Släktestabell T12:
    1–4 Människa, 5–7 Halvling, 8–9 Dvärg, 10 Alv, 11 Anka, 12 Vargfolk.
    """
    if 1 <= t12 <= 4:
        return RACES["Människa"]
    elif 5 <= t12 <= 7:
        return RACES["Halvling"]
    elif 8 <= t12 <= 9:
        return RACES["Dvärg"]
    elif t12 == 10:
        return RACES["Alv"]
    elif t12 == 11:
        return RACES["Anka"]
    elif t12 == 12:
        return RACES["Vargfolk"]
    else:
        raise ValueError("t12 måste vara 1–12")
