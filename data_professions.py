# data_professions.py
from dataclasses import dataclass
from typing import Optional


@dataclass
class Profession:
    name: str
    hero_ability_name: Optional[str]  # Magiker börjar utan hjälteförmåga
    # Här kan du lägga till t.ex.:
    # mandatory_trained_skills: list[str]
    # gear_options: list[list[str]]


PROFESSIONS: dict[str, Profession] = {
    "Bard": Profession(name="Bard", hero_ability_name="Tonkonst"),
    "Hantverkare": Profession(name="Hantverkare", hero_ability_name="Mästersmed / Mästersnickare (välj)"),
    "Jägare": Profession(name="Jägare", hero_ability_name="Stigfinnare"),
    "Krigare": Profession(name="Krigare", hero_ability_name="Stridsvana"),
    "Lärd": Profession(name="Lärd", hero_ability_name="Insikt"),
    "Magiker": Profession(name="Magiker", hero_ability_name=None),  # ersätts av magiskola
    "Nasare": Profession(name="Nasare", hero_ability_name="Kvartermästare"),
    "Riddare": Profession(name="Riddare", hero_ability_name="Förkämpe"),
    "Sjöfarare": Profession(name="Sjöfarare", hero_ability_name="Sjöben"),
    "Tjuv": Profession(name="Tjuv", hero_ability_name="Kattfot"),
}


def roll_random_profession(t10: int) -> Profession:
    """
    Yrken T10:
    1 Bard, 2 Hantverkare, 3 Jägare, 4 Krigare, 5 Lärd,
    6 Magiker, 7 Nasare, 8 Riddare, 9 Sjöfarare, 10 Tjuv.
    """
    mapping = {
        1: "Bard",
        2: "Hantverkare",
        3: "Jägare",
        4: "Krigare",
        5: "Lärd",
        6: "Magiker",
        7: "Nasare",
        8: "Riddare",
        9: "Sjöfarare",
        10: "Tjuv",
    }
    try:
        return PROFESSIONS[mapping[t10]]
    except KeyError:
        raise ValueError("t10 måste vara 1–10")
