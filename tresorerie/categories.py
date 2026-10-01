"""Catégorisation des opérations.

Version simple à base de mots-clés. Dans la vraie appli, c'est l'IA qui s'en charge.
"""

REGLES = {
    "Logement": ["LOYER", "EDF", "ASSURANCE HABITATION"],
    "Courses": ["CARREFOUR", "MONOPRIX", "LIDL", "BOULANGERIE"],
    "Transport": ["NAVIGO", "SNCF"],
    "Abonnements": ["FREE MOBILE"],
    "Loisirs": ["CINEMA"],
}


def categoriser(operation):
    """Renvoie la catégorie d'une opération."""
    if operation.montant > 0:
        return "Revenus"
    libelle = operation.libelle.upper()
    for categorie, mots_cles in REGLES.items():
        if any(mot in libelle for mot in mots_cles):
            return categorie
    return "Autre"
