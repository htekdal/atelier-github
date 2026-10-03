from datetime import date
from decimal import Decimal

from tresorerie.import_csv import lire_releve
from tresorerie.prevision import depense_journaliere_moyenne, periode


def test_prevision_commence_au_premier_jour():
    jours = periode(date(2026, 10, 1), date(2026, 12, 29))
    assert jours[0] == date(2026, 10, 1)


def test_prevision_inclut_le_dernier_jour():
    jours = periode(date(2026, 10, 1), date(2026, 12, 29))
    assert len(jours) == 90
    assert jours[-1] == date(2026, 12, 29)


def test_depense_journaliere_moyenne():
    operations = lire_releve("data/exemple_releve.csv")
    assert depense_journaliere_moyenne(operations) == Decimal("29.65")
