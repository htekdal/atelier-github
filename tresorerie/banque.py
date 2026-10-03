"""Connexion à l'API de la banque (simulée pour l'atelier)."""
import os


def charger_cle():
    """Lit la clé d'API dans la variable d'environnement BANQUE_API_KEY."""
    cle = os.environ.get("BANQUE_API_KEY")
    if not cle:
        raise RuntimeError("Variable BANQUE_API_KEY absente : renseigne-la dans ton fichier .env")
    return cle


def entetes_requete():
    """En-têtes HTTP à envoyer à l'API de la banque."""
    return {"Authorization": f"Bearer {charger_cle()}", "Accept": "application/json"}
