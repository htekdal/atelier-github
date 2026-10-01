"""Lecture des relevés bancaires au format CSV (séparateur ;, virgule décimale)."""
import csv
from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from pathlib import Path


@dataclass(frozen=True)
class Operation:
    date: date
    libelle: str
    montant: Decimal


def lire_montant(texte):
    """Convertit '1450,00' ou '-34,27' en Decimal."""
    return Decimal(texte.replace(" ", "").replace(",", "."))


def lire_releve(chemin):
    """Renvoie la liste des opérations d'un relevé, dans l'ordre du fichier."""
    operations = []
    with Path(chemin).open(encoding="utf-8") as fichier:
        for ligne in csv.DictReader(fichier, delimiter=";"):
            operations.append(
                Operation(
                    date=date.fromisoformat(ligne["date"]),
                    libelle=ligne["libelle"].strip(),
                    montant=lire_montant(ligne["montant"]),
                )
            )
    return operations
