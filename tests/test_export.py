from datetime import date
from decimal import Decimal

from tresorerie.export import exporter_categories, totaux_par_categorie
from tresorerie.import_csv import Operation


def op(libelle, montant):
    return Operation(date(2026, 9, 1), libelle, Decimal(montant))


OPERATIONS = [
    op("VIR SALAIRE", "1000"),
    op("PRLV LOYER", "-500"),
    op("CB CARREFOUR", "-20.50"),
    op("CB CARREFOUR", "-9.50"),
]


def test_totaux_par_categorie():
    totaux = totaux_par_categorie(OPERATIONS)
    assert totaux["Courses"] == Decimal("-30.00")
    assert totaux["Logement"] == Decimal("-500")
    assert totaux["Revenus"] == Decimal("1000")


def test_exporter_categories(tmp_path):
    chemin = exporter_categories(OPERATIONS, tmp_path / "export.csv")
    lignes = chemin.read_text(encoding="utf-8").splitlines()
    assert lignes[0] == "categorie;total"
    assert "Courses;-30,00" in lignes
