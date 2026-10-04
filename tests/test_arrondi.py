from decimal import Decimal

from tresorerie.soldes import solde_courant


def test_arrondi_demi_centime_au_superieur():
    # En comptabilité, 0,005 € s'arrondit à 0,01 € (et non à 0,00 €).
    assert solde_courant([], Decimal("0.005")) == Decimal("0.01")


def test_arrondi_demi_centime_negatif():
    assert solde_courant([], Decimal("-2.125")) == Decimal("-2.13")
