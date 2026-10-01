"""Calcul des soldes du compte."""
from decimal import Decimal, ROUND_HALF_UP


def solde_courant(operations, solde_initial=Decimal("0")):
    """Solde après application de toutes les opérations."""
    total = solde_initial + sum((op.montant for op in operations), Decimal("0"))
    solde = total.quantize(Decimal("0.01"))
    return solde


def formater_montant(montant):
    """Affiche un montant à la française : 1 234,56 €."""
    signe = "-" if montant < 0 else ""
    entier, decimales = f"{abs(montant):.2f}".split(".")
    groupes = []
    while len(entier) > 3:
        groupes.insert(0, entier[-3:])
        entier = entier[:-3]
    groupes.insert(0, entier)
    return f"{signe}{' '.join(groupes)},{decimales} €"
