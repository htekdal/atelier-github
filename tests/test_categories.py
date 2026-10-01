from datetime import date
from decimal import Decimal

import pytest

from tresorerie.categories import categoriser
from tresorerie.import_csv import Operation


@pytest.mark.parametrize(
    "libelle, attendu",
    [
        ("PRLV LOYER RESIDENCE", "Logement"),
        ("CB CARREFOUR CITY", "Courses"),
        ("CB LIDL", "Courses"),
        ("CB BOULANGERIE DU COIN", "Courses"),
        ("CB NAVIGO ABONNEMENT", "Transport"),
        ("CB SNCF CONNECT", "Transport"),
        ("CB MAGASIN INCONNU", "Autre"),
    ],
)
def test_categoriser_depenses(libelle, attendu):
    assert categoriser(Operation(date(2026, 9, 1), libelle, Decimal("-10"))) == attendu


def test_categoriser_revenu():
    assert categoriser(Operation(date(2026, 9, 1), "VIR SALAIRE", Decimal("100"))) == "Revenus"
