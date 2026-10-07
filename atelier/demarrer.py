"""Mission 0 : crée les labels, une issue par mission et le tableau de bord.

Peut être relancé sans risque : les missions existantes sont mises à jour avec la
dernière version de leur texte, sauf si tu as déjà commencé à cocher leurs étapes
ou si elles sont validées.
"""
import os
from pathlib import Path

import github_api as gh
import tableau

LABELS = {
    "mission": ("3446C9", "Mission de l'atelier"),
    "palier-1": ("BFD4F2", "Lire et naviguer"),
    "palier-2": ("A2C4F0", "Piloter l'IA"),
    "palier-3": ("7FAEEA", "Contrôler"),
    "palier-4": ("5B8FDF", "Réparer et protéger"),
    "pour-claude": ("C25A12", "Issue à confier à Claude Code"),
    "réussie": ("0B7F68", "Mission validée par le correcteur"),
    "tableau-de-bord": ("152036", "Suivi de progression de l'atelier"),
}

PIED = ("\n\n---\n_Coche les étapes au fur et à mesure. Bloqué ? Ouvre la section « Si tu bloques ». "
        "Quand tu as terminé, commente `/verifier` sur cette issue : le correcteur répond en une minute environ._")


def lire_mission(chemin):
    entete, corps = chemin.read_text(encoding="utf-8").split("\n---\n", 1)
    meta = dict(ligne.split(": ", 1) for ligne in entete.strip().splitlines())
    labels = [l.strip() for l in meta["labels"].split(",")]
    return meta["titre"].strip(), corps.strip() + PIED, labels


def main():
    for nom, (couleur, description) in LABELS.items():
        try:
            gh.post(gh.repo("/labels"), {"name": nom, "color": couleur, "description": description})
            print(f"Label créé : {nom}")
        except gh.ErreurAPI as erreur:
            if erreur.statut != 422:
                raise
            print(f"Label déjà présent : {nom}")

    existantes = {i["title"]: i for i in gh.get_tout(gh.repo("/issues"), {"state": "all"}) if "pull_request" not in i}
    lignes = ["## Missions de l'atelier", ""]
    for chemin in sorted(Path(__file__).parent.joinpath("missions").glob("*.md")):
        titre, corps, labels = lire_mission(chemin)
        issue = existantes.get(titre)
        if issue is None:
            issue = gh.post(gh.repo("/issues"), {"title": titre, "body": corps, "labels": labels})
            etat = "créée"
        elif issue.get("body") == corps:
            etat = "déjà à jour"
        elif "- [x]" in (issue.get("body") or "") or issue["state"] == "closed":
            etat = "conservée (déjà commencée ou validée)"
        else:
            gh.patch(gh.repo(f"/issues/{issue['number']}"), {"body": corps})
            etat = "mise à jour"
        print(f"#{issue['number']} {titre} : {etat}")
        lignes.append(f"- [#{issue['number']} {titre}]({issue['html_url']}) : {etat}")

    bord = tableau.mettre_a_jour()
    if bord:
        lignes += ["", f"Tableau de bord : [#{bord['number']}]({bord['html_url']})"]
    lignes += ["", "C'est parti : ouvre l'onglet **Issues**, épingle le tableau de bord, puis commence par la mission 01."]
    resume = os.environ.get("GITHUB_STEP_SUMMARY")
    if resume:
        Path(resume).write_text("\n".join(lignes), encoding="utf-8")


if __name__ == "__main__":
    main()
