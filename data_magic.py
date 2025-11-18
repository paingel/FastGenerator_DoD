# data_magic.py
from dataclasses import dataclass
from typing import Literal


MagicSchool = Literal["allman", "animism", "elementalism", "mentalism"]


@dataclass(frozen=True)
class Trick:
    name: str
    school: MagicSchool  # "allman" = allmän magi


@dataclass(frozen=True)
class Spell:
    name: str
    school: MagicSchool
    level: int  # 1, 2, 3, ...


# =========================
# TROLLERITRICK
# =========================
# OBS: Detta är bara ett EXEMPEL-URVAL.
# Fyll på alla namn från boken själv.

TRICKS: list[Trick] = [
    # Allmän magi – trolleritrick
    Trick("Hämta", "allman"),
    Trick("Knäpp", "allman"),
    Trick("Känna magi", "allman"),
    Trick("Laga kläder", "allman"),
    Trick("Ljus", "allman"),
    Trick("Öppna/stänga", "allman"),

    # Animism – trolleritrick
    Trick("Blomsterspår", "animism"),
    Trick("Frisyr", "animism"),
    Trick("Fågelsång", "animism"),
    Trick("Laga mat", "animism"),
    Trick("Städa", "animism"),

    # Elementalism – trolleritrick
    Trick("Rökpuff", "elementalism"),
    Trick("Tända", "elementalism"),
    Trick("Värma/kyla", "elementalism"),

    # Mentalism – trolleritrick
    Trick("Bromsa fall", "mentalism"),
    Trick("Låsa/låsa upp", "mentalism"),
    Trick("Magisk pall", "mentalism"),
]


# =========================
# BESVÄRJELSER
# =========================
# Här är ett litet urval – fyll på alla namn + rätt nivå från
# besvärjelselistan i regelboken. :contentReference[oaicite:2]{index=2}

SPELLS: list[Spell] = [
    # Allmän magi – nivå 1
    Spell("Beskyddare", "allman", 1),
    Spell("Skingra", "allman", 1),
    # (Fyll på fler allmänna nivå-1-besvärjelser här)

    # Animism – nivå 1 (exempel)
    Spell("Fördriva", "animism", 1),
    Spell("Ljungeld", "animism", 1),
    Spell("Läka", "animism", 1),
    # Lägg till resten + nivåer 2,3 allteftersom du behöver dem

    # Elementalism – nivå 1 (exempel)
    Spell("Flamma", "elementalism", 1),
    Spell("Frost", "elementalism", 1),
    Spell("Pelare", "elementalism", 1),

    # Mentalism – nivå 1 (exempel)
    Spell("Fjärrsyn", "mentalism", 1),
    Spell("Lyft", "mentalism", 1),
    Spell("Långstige", "mentalism", 1),

    # Exempel på högre nivå (bara för framtida bruk i kampanj)
    # Spell("Åskvigg", "animism", 3),
    # Spell("Eldklot", "elementalism", 3),
    # Spell("Teleportera", "mentalism", 3),
]


# =========================
# HJÄLPFUNKTIONER
# =========================

def get_tricks_for_school_or_general(school: MagicSchool) -> list[Trick]:
    """
    Alla trolleritrick som en magiker får välja från vid start:
    - allmän magi
    - den egna magiskolan
    """
    return [t for t in TRICKS if t.school in ("allman", school)]


def get_level1_spells_for_school_or_general(school: MagicSchool) -> list[Spell]:
    """
    Alla Nivå-1-besvärjelser från:
    - allmän magi
    - den egna magiskolan
    """
    return [
        s for s in SPELLS
        if s.level == 1 and s.school in ("allman", school)
    ]
