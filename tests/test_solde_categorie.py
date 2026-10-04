from datetime import date
from decimal import Decimal

from tresorerie.import_csv import Operation
from tresorerie.soldes import solde_par_categorie


def op(libelle, montant):
    return Operation(date(2026, 9, 1), libelle, Decimal(montant))


def test_solde_par_categorie():
    totaux = solde_par_categorie([op("PRLV LOYER", "-500"), op("CB CARREFOUR", "-20"), op("CB CARREFOUR", "-5")])
    assert totaux == {"Logement": Decimal("-500"), "Courses": Decimal("-25")}
