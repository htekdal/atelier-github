"""Export des totaux par catégorie au format CSV."""
import csv
from decimal import Decimal
from pathlib import Path

from tresorerie.categories import categoriser


def totaux_par_categorie(operations):
    """Somme des montants par catégorie, triée par nom de catégorie."""
    totaux = {}
    for op in operations:
        categorie = categoriser(op)
        totaux[categorie] = totaux.get(categorie, Decimal("0")) + op.montant
    return dict(sorted(totaux.items()))


def exporter_categories(operations, chemin):
    """Écrit un CSV categorie;total (virgule décimale) et renvoie son chemin."""
    with Path(chemin).open("w", encoding="utf-8", newline="") as fichier:
        ecrivain = csv.writer(fichier, delimiter=";")
        ecrivain.writerow(["categorie", "total"])
        for categorie, total in totaux_par_categorie(operations).items():
            ecrivain.writerow([categorie, f"{total:.2f}".replace(".", ",")])
    return chemin
