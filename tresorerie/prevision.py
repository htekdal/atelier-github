"""Prévision de trésorerie : projette une dépense moyenne jour par jour."""
from datetime import timedelta
from decimal import Decimal


def periode(debut, fin):
    """Toutes les dates de debut à fin, bornes incluses."""
    return [debut + timedelta(days=i) for i in range((fin - debut).days)]


def depense_journaliere_moyenne(operations):
    """Moyenne des dépenses par jour sur la période couverte par le relevé."""
    depenses = sum((-op.montant for op in operations if op.montant < 0), Decimal("0"))
    jours = (operations[-1].date - operations[0].date).days + 1
    return (depenses / jours).quantize(Decimal("0.01"))


def projeter_solde(solde, depense_par_jour, debut, fin):
    """Solde estimé à la date fin si l'on dépense depense_par_jour chaque jour."""
    return solde - depense_par_jour * len(periode(debut, fin))
