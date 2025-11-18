# generator.py
import random
from typing import List

from dice import roll_4d6_drop_lowest, roll_dice
from data_races import roll_random_race
from data_ages import roll_random_age
from data_professions import roll_random_profession
from data_magic import (
    MagicSchool,
    get_tricks_for_school_or_general,
    get_level1_spells_for_school_or_general,
)
from models import AttributeSet, SecondaryStats, Character


BASE_PROFESSION_TRAINED_SKILLS = 6


def generate_base_attributes() -> AttributeSet:
    """Slå fram sex grundegenskaper enligt 4T6, ta bort lägsta, slumpa placering."""
    rolls: List[int] = [roll_4d6_drop_lowest() for _ in range(6)]
    random.shuffle(rolls)
    return AttributeSet(
        STY=rolls[0],
        FYS=rolls[1],
        SMI=rolls[2],
        INT=rolls[3],
        PSY=rolls[4],
        KAR=rolls[5],
    )


def apply_age_modifiers(attrs: AttributeSet, age) -> AttributeSet:
    def clamp(x: int) -> int:
        return max(3, min(18, x))

    return AttributeSet(
        STY=clamp(attrs.STY + age.str_mod),
        FYS=clamp(attrs.FYS + age.fys_mod),
        SMI=clamp(attrs.SMI + age.smi_mod),
        INT=clamp(attrs.INT + age.int_mod),
        PSY=clamp(attrs.PSY + age.psy_mod),
        KAR=attrs.KAR,
    )


def smi_move_modifier(smi: int) -> int:
    if 1 <= smi <= 6:
        return -4
    elif 7 <= smi <= 9:
        return -2
    elif 13 <= smi <= 15:
        return +2
    elif 16 <= smi <= 18:
        return +4
    else:
        return 0


def damage_bonus_from_attr(value: int) -> str:
    if value <= 12:
        return "-"
    elif 13 <= value <= 16:
        return "+T4"
    else:
        return "+T6"


def compute_secondary(race, attrs: AttributeSet) -> SecondaryStats:
    move = race.base_move + smi_move_modifier(attrs.SMI)
    kp_max = attrs.FYS
    vp_max = attrs.PSY
    db_str = damage_bonus_from_attr(attrs.STY)
    db_smi = damage_bonus_from_attr(attrs.SMI)
    return SecondaryStats(
        move=move,
        kp_max=kp_max,
        vp_max=vp_max,
        damage_bonus_str=db_str,
        damage_bonus_smi=db_smi,
    )


def generate_random_name(race) -> str:
    return random.choice(race.example_names)


# =========================
# MAGI-SPECIFIKT
# =========================

MAGIC_SCHOOLS: list[tuple[MagicSchool, str]] = [
    ("animism", "Animism"),
    ("elementalism", "Elementalism"),
    ("mentalism", "Mentalism"),
]


def choose_random_magic_school() -> tuple[MagicSchool, str]:
    """
    Välj slumpad magiskola:
    returnerar (intern_kod, snyggt_namn)
    """
    return random.choice(MAGIC_SCHOOLS)


def assign_magic_to_character(char: Character) -> None:
    """
    Om rollpersonen är magiker:
    - välj magiskola
    - välj 3 trolleritrick (allmän + skola)
    - välj 3 nivå-1-besvärjelser (allmän + skola)
    Sparas direkt på char.
    :contentReference[oaicite:4]{index=4}
    """
    if char.profession_name != "Magiker":
        return

    school_code, school_label = choose_random_magic_school()
    char.magic_school_name = school_label

    # Trolleritrick
    possible_tricks = get_tricks_for_school_or_general(school_code)
    if len(possible_tricks) >= 3:
        chosen_tricks = random.sample(possible_tricks, 3)
    else:
        chosen_tricks = possible_tricks  # om du inte hunnit fylla alla listor

    char.known_tricks = [t.name for t in chosen_tricks]

    # Nivå-1-besvärjelser
    possible_spells = get_level1_spells_for_school_or_general(school_code)
    if len(possible_spells) >= 3:
        chosen_spells = random.sample(possible_spells, 3)
    else:
        chosen_spells = possible_spells

    char.known_spells = [s.name for s in chosen_spells]


# =========================
# HUVUDGENERATOR
# =========================

def generate_character() -> Character:
    # Släkte, yrke, ålder
    race = roll_random_race(roll_dice(1, 12)[0])
    prof = roll_random_profession(roll_dice(1, 10)[0])
    age = roll_random_age(roll_dice(1, 6)[0])

    # Grundegenskaper
    base_attrs = generate_base_attributes()
    attrs = apply_age_modifiers(base_attrs, age)

    # Sekundära egenskaper
    secondary = compute_secondary(race, attrs)

    # Namn
    name = generate_random_name(race)

    # Hjälteförmåga (magiker får hjälteförmåga via magiskola i praktiken,
    # men vi låter yrkesdata bestämma som tidigare)
    hero_ability = prof.hero_ability_name

    gear_summary = f"Standardutrustning för {prof.name} (komplettera enligt regelboken)."

    # Färdigheter: alla rollpersoner får 6 tränade färdigheter via yrket
    # och sedan bonus utifrån ålder.
    skill_values = {
        "base_trained_skills": BASE_PROFESSION_TRAINED_SKILLS,
        "extra_trained_skills": age.extra_trained_skills,
        "total_trained_skills": BASE_PROFESSION_TRAINED_SKILLS + age.extra_trained_skills,
    }

    character = Character(
        name=name,
        race=race,
        profession_name=prof.name,
        age=age,
        attributes=attrs,
        secondary=secondary,
        hero_ability_name=hero_ability,
        skill_values=skill_values,
        gear_summary=gear_summary,
    )

    # === NYTT: om magiker, ge magiskola + 3 trick + 3 besvärjelser ===
    assign_magic_to_character(character)

    return character
