from datetime import date
from decimal import Decimal

from tresorerie.import_csv import Operation
from tresorerie.soldes import formater_montant, solde_courant


def op(montant):
    return Operation(date(2026, 9, 1), "TEST", Decimal(montant))


def test_solde_vide():
    assert solde_courant([], Decimal("300")) == Decimal("300.00")


def test_solde_operations():
    assert solde_courant([op("100"), op("-40.50")]) == Decimal("59.50")


def test_formater_montant():
    assert formater_montant(Decimal("1234.5")) == "1 234,50 €"
    assert formater_montant(Decimal("-7")) == "-7,00 €"
