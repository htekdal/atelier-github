"""Mission 0 : crée les labels et une issue par mission (sans doublon)."""
import os
from pathlib import Path

import github_api as gh

LABELS = {
    "mission": ("3446C9", "Mission de l'atelier"),
    "palier-1": ("BFD4F2", "Lire et naviguer"),
    "palier-2": ("A2C4F0", "Piloter l'IA"),
    "palier-3": ("7FAEEA", "Contrôler"),
    "palier-4": ("5B8FDF", "Réparer et protéger"),
    "pour-claude": ("C25A12", "Issue à confier à Claude Code"),
    "réussie": ("0B7F68", "Mission validée par le correcteur"),
}


def lire_mission(chemin):
    entete, corps = chemin.read_text(encoding="utf-8").split("\n---\n", 1)
    meta = dict(ligne.split(": ", 1) for ligne in entete.strip().splitlines())
    labels = [l.strip() for l in meta["labels"].split(",")]
    pied = "\n\n---\n_Quand tu as terminé, commente `/verifier` sur cette issue. Le correcteur répond en une minute environ._"
    return meta["titre"].strip(), corps.strip() + pied, labels


def main():
    for nom, (couleur, description) in LABELS.items():
        try:
            gh.post(gh.repo("/labels"), {"name": nom, "color": couleur, "description": description})
            print(f"Label créé : {nom}")
        except gh.ErreurAPI as erreur:
            if erreur.statut != 422:
                raise
            print(f"Label déjà présent : {nom}")

    existantes = {i["title"] for i in gh.get_tout(gh.repo("/issues"), {"state": "all"})}
    lignes = ["## Missions de l'atelier", ""]
    for chemin in sorted(Path(__file__).parent.joinpath("missions").glob("*.md")):
        titre, corps, labels = lire_mission(chemin)
        if titre in existantes:
            print(f"Déjà créée : {titre}")
            lignes.append(f"- {titre} (déjà présente)")
            continue
        issue = gh.post(gh.repo("/issues"), {"title": titre, "body": corps, "labels": labels})
        print(f"Créée : #{issue['number']} {titre}")
        lignes.append(f"- [#{issue['number']} {titre}]({issue['html_url']})")

    lignes += ["", "C'est parti : ouvre l'onglet **Issues** et commence par la mission 01."]
    resume = os.environ.get("GITHUB_STEP_SUMMARY")
    if resume:
        Path(resume).write_text("\n".join(lignes), encoding="utf-8")


if __name__ == "__main__":
    main()
