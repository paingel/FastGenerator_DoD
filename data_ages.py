# data_ages.py
from dataclasses import dataclass


@dataclass
class AgeCategory:
    name: str
    extra_trained_skills: int  # utöver 6 yrkes-bundna
    str_mod: int = 0
    fys_mod: int = 0
    smi_mod: int = 0
    int_mod: int = 0
    psy_mod: int = 0


AGES: dict[str, AgeCategory] = {
    "Ung": AgeCategory(
        name="Ung",
        extra_trained_skills=2,
        smi_mod=+1,
        fys_mod=+1,
    ),
    "Medelålders": AgeCategory(
        name="Medelålders",
        extra_trained_skills=4,
    ),
    "Gammal": AgeCategory(
        name="Gammal",
        extra_trained_skills=6,
        str_mod=-2,
        smi_mod=-2,
        fys_mod=-2,
        int_mod=+1,
        psy_mod=+1,
    ),
}


def roll_random_age(t6: int) -> AgeCategory:
    """
    T6 ÅLDER:
    1–3 Ung, 4–5 Medelålders, 6 Gammal.
    """
    if 1 <= t6 <= 3:
        return AGES["Ung"]
    elif 4 <= t6 <= 5:
        return AGES["Medelålders"]
    elif t6 == 6:
        return AGES["Gammal"]
    else:
        raise ValueError("t6 måste vara 1–6")
