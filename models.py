# models.py
from dataclasses import dataclass, field
from typing import Dict

from data_races import Race
from data_ages import AgeCategory


@dataclass
class AttributeSet:
    STY: int
    FYS: int
    SMI: int
    INT: int
    PSY: int
    KAR: int


@dataclass
class SecondaryStats:
    move: int
    kp_max: int
    vp_max: int
    damage_bonus_str: str
    damage_bonus_smi: str


@dataclass
class Character:
    name: str
    race: Race
    profession_name: str
    age: AgeCategory
    attributes: AttributeSet
    secondary: SecondaryStats

    hero_ability_name: str | None = None
    skill_values: Dict[str, int] = field(default_factory=dict)
    weakness: str | None = None
    gear_summary: str | None = None

    # === NYTT: MAGI ===
    magic_school_name: str | None = None
    known_tricks: list[str] = field(default_factory=list)
    known_spells: list[str] = field(default_factory=list)

    def to_pdf_field_dict(self) -> Dict[str, str]:
        """
        Mappa rollpersonen till ett dict {pdf_fältnamn: värde}
        Anpassa nycklarna till fältnamnen i din PDF-mall.
        """
        return {
            "Name": self.name,
            "Race": self.race.name,
            "Profession": self.profession_name,
            "Age": self.age.name,

            "STY": str(self.attributes.STY),
            "FYS": str(self.attributes.FYS),
            "SMI": str(self.attributes.SMI),
            "INT": str(self.attributes.INT),
            "PSY": str(self.attributes.PSY),
            "KAR": str(self.attributes.KAR),

            "KP": str(self.secondary.kp_max),
            "VP": str(self.secondary.vp_max),
            "Move": str(self.secondary.move),
            "SB_STY": self.secondary.damage_bonus_str,
            "SB_SMI": self.secondary.damage_bonus_smi,

            "HeroAbility": self.hero_ability_name or "",
            "Gear": self.gear_summary or "",

            # === NYTT: PDF-fält för magi ===
            "MagicSchool": self.magic_school_name or "",
            "Tricks": "\n".join(self.known_tricks),
            "Spells": "\n".join(self.known_spells),
        }
