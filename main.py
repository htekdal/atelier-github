"""Point d'entrée de l'appli : python main.py"""
import sys
from decimal import Decimal

from tresorerie.export import exporter_categories
from tresorerie.import_csv import lire_releve
from tresorerie.soldes import formater_montant, solde_courant

RELEVE = "data/exemple_releve.csv"
SOLDE_INITIAL = Decimal("300.00")


def resume(operations):
    solde = solde_courant(operations, SOLDE_INITIAL)
    print(f"{len(operations)} opérations importées")
    print(f"Solde au {operations[-1].date:%d/%m/%Y} : {formater_montant(solde)}")


def main(args):
    operations = lire_releve(RELEVE)
    commande = args[0] if args else "resume"
    if commande == "resume":
        resume(operations)
    elif commande == "export":
        chemin = exporter_categories(operations, "export_categories.csv")
        print(f"Totaux par catégorie exportés dans {chemin}")
    else:
        print(f"Commande inconnue : {commande}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
