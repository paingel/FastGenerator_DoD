# main.py
from generator import generate_character
from pdf_export import fill_character_sheet


def main():
    # 1. Skapa slumpad rollperson
    char = generate_character()

    # 2. Skriv ut till konsolen
    print("==== Ny slumpad rollperson ====")
    print(f"Namn: {char.name}")
    print(f"Släkte: {char.race.name} ({char.race.ability_name})")
    print(f"Yrke: {char.profession_name}")
    print(f"Ålder: {char.age.name}")
    print()
    print(f"STY {char.attributes.STY}  FYS {char.attributes.FYS}  SMI {char.attributes.SMI}")
    print(f"INT {char.attributes.INT}  PSY {char.attributes.PSY}  KAR {char.attributes.KAR}")
    print()
    print(f"KP: {char.secondary.kp_max}  VP: {char.secondary.vp_max}")
    print(f"Förflyttning: {char.secondary.move}")
    print(f"Skadebonus STY: {char.secondary.damage_bonus_str}, SMI: {char.secondary.damage_bonus_smi}")
    print()
    print(f"Hjälteförmåga: {char.hero_ability_name or 'Ingen (magiker?)'}")
    print(f"Utrustning: {char.gear_summary}")

    if char.profession_name == "Magiker":
        print()
        print(f"Magiskola: {char.magic_school_name}")
        print("Trolleritrick:")
        for t in char.known_tricks:
            print(f"  - {t}")
        print("Besvärjelser (nivå 1):")
        for s in char.known_spells:
            print(f"  - {s}")

    # 3. Skapa ifylld PDF (ställ in dina faktiska filnamn här)
    template_pdf = "dod_karaktar_template.pdf"   # din form-variant av rollformuläret
    output_pdf = "dod_karaktar_ifylld.pdf"
    try:
        fill_character_sheet(template_pdf, output_pdf, char)
        print(f"\nPDF sparad som: {output_pdf}")
    except FileNotFoundError:
        print("\nKunde inte hitta PDF-mallen – hoppar över PDF-exporten.")
        print("Skapa/placera din form-PDF och uppdatera sökvägen i main.py.")


if __name__ == "__main__":
    main()
