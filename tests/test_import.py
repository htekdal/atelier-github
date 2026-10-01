from decimal import Decimal

from tresorerie.import_csv import lire_montant, lire_releve


def test_lire_montant_virgule_decimale():
    assert lire_montant("-34,27") == Decimal("-34.27")


def test_lire_montant_espaces():
    assert lire_montant("1 450,00") == Decimal("1450.00")


def test_lire_releve_exemple():
    operations = lire_releve("data/exemple_releve.csv")
    assert len(operations) == 14
    assert operations[0].libelle == "VIR SEPA ATELIER DUPONT SALAIRE"
