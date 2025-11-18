# pdf_export.py
from pathlib import Path
from typing import Union

from PyPDF2 import PdfReader, PdfWriter

from models import Character


PathLike = Union[str, Path]


def fill_character_sheet(template_path: PathLike, output_path: PathLike, character: Character) -> None:
    """
    Fyller i en befintlig PDF-formulärmall med data från Character.
    Kräver att PDF:en har AcroForm-fält med kända namn.
    """
    template_path = Path(template_path)
    output_path = Path(output_path)

    reader = PdfReader(str(template_path))
    writer = PdfWriter()

    # Kopiera alla sidor
    for page in reader.pages:
        writer.add_page(page)

    field_values = character.to_pdf_field_dict()

    # Uppdatera formulärfälten på första sidan (eller alla sidor om du föredrar det)
    writer.update_page_form_field_values(writer.pages[0], field_values)

    # Kopiera över formdefinitionen om den finns
    if "/AcroForm" in reader.trailer["/Root"]:
        writer._root_object.update(
            {"/AcroForm": reader.trailer["/Root"]["/AcroForm"]}
        )

    with open(output_path, "wb") as f:
        writer.write(f)
