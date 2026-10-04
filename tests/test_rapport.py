from tresorerie.import_csv import lire_releve
from tresorerie.rapport import code_controle, rapport_mensuel


def test_rapport_contient_total():
    texte = rapport_mensuel(lire_releve("data/exemple_releve.csv"))
    assert "Total des dépenses" in texte


def test_code_controle_format():
    code = code_controle(lire_releve("data/exemple_releve.csv"))
    assert code.startswith("RM-") and len(code) == 7
