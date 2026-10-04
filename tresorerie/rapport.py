"""Rapport mensuel des dépenses par catégorie."""
from decimal import Decimal

from tresorerie.categories import categoriser
from tresorerie.soldes import formater_montant


def code_controle(operations):
    """Petit code calculé à partir des opérations, pour vérifier qu'un rapport est complet."""
    somme = sum(int(abs(op.montant) * 100) * (i + 1) for i, op in enumerate(operations))
    return f"RM-{somme % 9973:04d}"


def rapport_mensuel(operations):
    """Texte du rapport : dépenses par catégorie, total et code de contrôle."""
    depenses = [op for op in operations if op.montant < 0]
    par_categorie = {}
    for op in depenses:
        categorie = categoriser(op)
        par_categorie[categorie] = par_categorie.get(categorie, Decimal("0")) + op.montant
    total = sum(par_categorie.values(), Decimal("0"))

    mois = operations[0].date
    lignes = [f"Rapport des dépenses · {mois:%m/%Y}", ""]
    for categorie, montant in sorted(par_categorie.items(), key=lambda x: x[1]):
        part = montant / total * 100
        lignes.append(f"  {categorie:<12} {formater_montant(montant):>12}  ({part:.0f} %)")
    lignes += ["", f"Total des dépenses : {formater_montant(total)}", f"Code de contrôle : {code_controle(operations)}"]
    return "\n".join(lignes)
