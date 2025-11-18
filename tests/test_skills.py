from unittest.mock import patch

from data_ages import AGES
from data_professions import PROFESSIONS
from data_races import RACES
from generator import generate_character
from models import AttributeSet


def _generate_character_for_age(age_key: str):
    base_attrs = AttributeSet(STY=10, FYS=10, SMI=10, INT=10, PSY=10, KAR=10)

    with patch("generator.roll_random_race", return_value=RACES["Människa"]), \
        patch("generator.roll_random_profession", return_value=PROFESSIONS["Bard"]), \
        patch("generator.roll_random_age", return_value=AGES[age_key]), \
        patch("generator.generate_base_attributes", return_value=base_attrs), \
        patch("generator.generate_random_name", return_value="Test"), \
        patch("generator.assign_magic_to_character", return_value=None):
        return generate_character()


def test_age_categories_give_different_trained_skills():
    young = _generate_character_for_age("Ung")
    middle = _generate_character_for_age("Medelålders")
    old = _generate_character_for_age("Gammal")

    assert young.skill_values["total_trained_skills"] == 8
    assert middle.skill_values["total_trained_skills"] == 10
    assert old.skill_values["total_trained_skills"] == 12

    assert young.skill_values["extra_trained_skills"] == 2
    assert middle.skill_values["extra_trained_skills"] == 4
    assert old.skill_values["extra_trained_skills"] == 6
