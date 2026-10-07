"""Tableau de bord : une issue qui liste les missions et coche celles qui sont validées."""
import github_api as gh

TITRE = "Tableau de bord de l'atelier"
LABEL = "tableau-de-bord"
PALIERS = {
    "palier-1": "Palier 1 · Lire et naviguer",
    "palier-2": "Palier 2 · Piloter l'IA",
    "palier-3": "Palier 3 · Contrôler",
    "palier-4": "Palier 4 · Réparer et protéger",
}


def missions():
    issues = gh.get_tout(gh.repo("/issues"), {"labels": "mission", "state": "all"})
    return sorted((i for i in issues if "pull_request" not in i), key=lambda i: i["title"])


def labels(issue):
    return {l["name"] for l in issue.get("labels", [])}


def corps(liste):
    faites = sum("réussie" in labels(i) for i in liste)
    lignes = [
        f"**Progression : {faites} / {len(liste)} missions validées.**",
        "",
        "Le correcteur coche une mission ici dès que `/verifier` la valide. Ne modifie pas cette issue à la main :",
        "elle est réécrite à chaque validation. Pour suivre tes étapes, coche les cases **dans chaque mission**.",
        "",
        "Astuce : épingle cette issue (colonne de droite › **Pin issue**) pour la garder en haut de l'onglet Issues.",
    ]
    for label, titre in PALIERS.items():
        du_palier = [i for i in liste if label in labels(i)]
        if not du_palier:
            continue
        lignes += ["", f"### {titre}", ""]
        lignes += [f"- [{'x' if 'réussie' in labels(i) else ' '}] #{i['number']}" for i in du_palier]
    return "\n".join(lignes)


def mettre_a_jour():
    liste = missions()
    if not liste:
        return None
    existants = [i for i in gh.get_tout(gh.repo("/issues"), {"labels": LABEL, "state": "all"}) if "pull_request" not in i]
    texte = corps(liste)
    if existants:
        return gh.patch(gh.repo(f"/issues/{existants[0]['number']}"), {"body": texte})
    return gh.post(gh.repo("/issues"), {"title": TITRE, "body": texte, "labels": [LABEL]})
