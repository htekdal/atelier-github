"""Correcteur automatique des missions de l'atelier.

Déclenché par un commentaire /verifier sur une issue de mission. Examine l'état
du dépôt via git et l'API GitHub, puis répond en commentaire.
"""
import os
import re
import subprocess
import unicodedata
from decimal import Decimal
from pathlib import Path

import github_api as gh
import tableau

RACINE = Path(__file__).resolve().parent.parent
PROPRIETAIRE = gh.REPO.split("/")[0]
NUMERO = int(os.environ.get("ISSUE_NUMBER", "0"))
TITRE = os.environ.get("ISSUE_TITLE", "")


# ---------- outils ----------

def norm(texte):
    texte = unicodedata.normalize("NFKD", texte or "")
    texte = "".join(c for c in texte if not unicodedata.combining(c))
    return texte.replace("’", "'").lower()


def humain(objet):
    return objet.get("user", {}).get("type") == "User"


def git(*args):
    return subprocess.run(["git", *args], cwd=RACINE, capture_output=True, text=True, check=True).stdout


def fichier_main(chemin):
    p = RACINE / chemin
    return p.read_text(encoding="utf-8") if p.exists() else None


def reponses():
    """Lignes « clé: valeur » des commentaires humains de l'issue (la dernière gagne)."""
    resultat = {}
    for commentaire in gh.get_tout(gh.repo(f"/issues/{NUMERO}/comments")):
        if not humain(commentaire):
            continue
        for ligne in commentaire["body"].splitlines():
            if ":" in ligne:
                cle, valeur = ligne.split(":", 1)
                cle = norm(cle).strip(" `*->#")
                if valeur.strip():
                    resultat[cle] = valeur.strip()
    return resultat


def prs_de(branche):
    return gh.get_tout(gh.repo("/pulls"), {"state": "all", "head": f"{PROPRIETAIRE}:{branche}"})


def toutes_les_prs():
    return gh.get_tout(gh.repo("/pulls"), {"state": "all"})


def annulee(pr, toutes):
    """Vrai si une PR « Revert » de cette PR a été fusionnée."""
    return any(p["merged_at"] and p["title"].startswith("Revert") and pr["title"] in p["title"] for p in toutes)


def pas_fusionnee_ou_annulee(prs, c):
    toutes = toutes_les_prs()
    for p in prs:
        if p["merged_at"]:
            if not annulee(p, toutes):
                return False
            c.note(f"La PR #{p['number']} a été fusionnée puis annulée avec Revert : c'est accepté, et c'était le bon réflexe.")
    return True


def commentaires_relecture(numero):
    """Commentaires sur des lignes + revues avec un texte, par un humain."""
    lignes = [c for c in gh.get_tout(gh.repo(f"/pulls/{numero}/comments")) if humain(c)]
    revues = [r for r in gh.get_tout(gh.repo(f"/pulls/{numero}/reviews")) if humain(r) and r.get("body")]
    return lignes + revues


def commentaires_conversation(numero):
    return [c for c in gh.get_tout(gh.repo(f"/issues/{numero}/comments")) if humain(c)]


def nb_parents(sha):
    try:
        return len(git("rev-list", "--parents", "-n", "1", sha).split()) - 1
    except (subprocess.CalledProcessError, TypeError):
        return None


def operations_releve():
    lignes = fichier_main("data/exemple_releve.csv").strip().splitlines()[1:]
    return [Decimal(l.split(";")[2].replace(" ", "").replace(",", ".")) for l in lignes]


class Correction:
    def __init__(self):
        self.points, self.notes = [], []

    def verifie(self, ok, texte, indice=""):
        self.points.append((bool(ok), texte, indice))
        return bool(ok)

    def note(self, texte):
        self.notes.append(texte)

    @property
    def reussie(self):
        return bool(self.points) and all(ok for ok, _, _ in self.points)


def note_squash(c, pr):
    if pr and nb_parents(pr.get("merge_commit_sha")) == 2:
        c.note("Tu as fusionné avec « Create a merge commit ». Ce n'est pas faux, mais essaie « Squash and merge » la prochaine fois : un commit propre par PR sur main.")


# ---------- missions ----------

def m01(c):
    rep = reponses()
    if not rep:
        c.note("Je ne trouve pas tes réponses. Copie le modèle de l'issue dans un commentaire et complète chaque ligne.")
    cible = [ligne.split("\t")[0] for ligne in git("log", "--format=%H\t%s").splitlines()
             if ligne.split("\t", 1)[1] == "feat: import des relevés CSV"]
    proposes = [s.lower() for s in re.findall(r"[0-9a-fA-F]{7,40}", rep.get("sha", ""))]
    c.verifie(cible and any(cible[0].startswith(s) for s in proposes),
              "SHA du commit « feat: import des relevés CSV »",
              "Dans l'historique (icône d'horloge), le SHA court est le code de 7 caractères à droite du commit.")
    c.verifie("soldes.py" in rep.get("fichier", ""),
              "Fichier qui définit `solde_courant`",
              "Cherche « def solde_courant » avec la recherche du dépôt, ou ouvre les fichiers du dossier tresorerie/.")
    attendu = str(len(operations_releve()))
    c.verifie(attendu in re.findall(r"\d+", rep.get("operations", "")),
              "Nombre d'opérations du relevé",
              "Compte les lignes du tableau de data/exemple_releve.csv, sans la ligne d'en-tête.")


def m02(c):
    readme = fichier_main("README.md") or ""
    c.verifie("(ton pseudo ici)" not in readme, "README.md modifié sur main",
              "Remplace « (ton pseudo ici) » par ton pseudo dans la section Équipe.")
    candidates = [p for p in toutes_les_prs() if p["merged_at"] and not p["head"]["ref"].startswith(("ia/", "revert-"))]
    pr = next((p for p in candidates
               if any(f["filename"] == "README.md" for f in gh.get_tout(gh.repo(f"/pulls/{p['number']}/files")))), None)
    c.verifie(pr, "La modification est arrivée sur main par une pull request fusionnée",
              "Au moment du commit, choisis « Create a new branch for this commit and start a pull request », puis fusionne la PR.")
    note_squash(c, pr)


def m03(c):
    issues = [i for i in gh.get_tout(gh.repo("/issues"), {"labels": "pour-claude", "state": "all"}) if "pull_request" not in i]
    c.verifie(issues, "Une issue porte le label `pour-claude`",
              "Dans la colonne de droite de ton issue : Labels › pour-claude.")
    corps = [norm(i.get("body")) for i in issues]
    titres = ("## contexte", "## objectif", "## criteres d'acceptation")
    c.verifie(any(all(t in b for t in titres) for b in corps),
              "Les trois sections Contexte, Objectif et Critères d'acceptation sont présentes",
              "Copie exactement les titres du modèle, avec les ## devant.")
    c.verifie(any(len(re.findall(r"- \[[ x]\]", b)) >= 2 for b in corps),
              "Au moins deux critères d'acceptation sous forme de cases à cocher",
              "Chaque critère commence par `- [ ]`.")


def m04(c):
    prs = prs_de("ia/export-csv")
    fusionnees = [p for p in prs if p["merged_at"]]
    c.verifie(prs, "Une pull request existe pour `ia/export-csv`",
              "Pull requests › New pull request › base: main, compare: ia/export-csv.")
    c.verifie(sum(len(commentaires_relecture(p["number"])) for p in prs) >= 1,
              "Au moins un commentaire de relecture",
              "Dans Files changed, clique sur le + bleu à gauche d'une ligne, Start a review, puis Finish your review › Comment › Submit review.")
    c.verifie(fusionnees, "La pull request est fusionnée", "Une fois le check vert : Squash and merge.")
    note_squash(c, fusionnees[0] if fusionnees else None)


def m05(c):
    rep = reponses()
    prs = prs_de("ia/prevision-90j")
    c.verifie(prs, "Une pull request existe pour `ia/prevision-90j`",
              "Pull requests › New pull request › compare: ia/prevision-90j.")
    c.verifie(prs and pas_fusionnee_ou_annulee(prs, c), "La pull request n'a pas été fusionnée",
              "Une PR au check rouge ne se fusionne pas. Si c'est déjà fait, annule-la avec le bouton Revert de la PR fusionnée (voir mission 9).")
    commentaires = sum(len(commentaires_conversation(p["number"])) + len(commentaires_relecture(p["number"])) for p in prs)
    c.verifie(commentaires >= 1, "Un commentaire sur la PR décrit le problème",
              "Onglet Conversation de la PR : écris quel test échoue, ce qu'il attendait et ce qu'il a obtenu.")
    c.verifie("test_prevision_inclut_le_dernier_jour" in rep.get("test", ""),
              "Nom exact du test en échec",
              "Clique sur Details à côté du check, déplie « Run pytest -v » et cherche la ligne FAILED.")


def m06(c):
    rep = reponses()
    prs = prs_de("ia/connexion-banque")
    c.verifie(prs, "Une pull request existe pour `ia/connexion-banque`", "Ouvre-la pour inspecter ses fichiers.")
    c.verifie(prs and all(p["state"] == "closed" for p in prs) and pas_fusionnee_ou_annulee(prs, c),
              "La pull request est fermée sans être fusionnée",
              "Bouton Close pull request, en bas de la conversation. Si tu l'as fusionnée, annule-la avec Revert (voir mission 9).")
    lignes = [l.strip() for l in (fichier_main(".gitignore") or "").splitlines()]
    c.verifie(any(l in (".env", "/.env", "*.env", ".env*") for l in lignes),
              "`.env` est listé dans .gitignore sur main",
              "Modifie .gitignore via une branche et une PR (comme en mission 2), puis fusionne.")
    fichiers = norm(rep.get("fichiers", ""))
    c.verifie(".env" in fichiers and "releve_reel" in fichiers, "Les deux fichiers interdits sont identifiés",
              "Dans Files changed, regarde l'arborescence : un fichier de secrets et un fichier de données réelles.")
    try:
        gh.get(gh.repo("/branches/ia%2Fconnexion-banque"))
        c.note("La branche `ia/connexion-banque` existe encore, avec la clé et les données. Supprime-la depuis la PR fermée (Delete branch).")
    except gh.ErreurAPI:
        pass


def m07(c):
    rep = reponses()
    montants = operations_releve()
    somme = sum(int(abs(m) * 100) * (i + 1) for i, m in enumerate(montants))
    attendu = f"RM-{somme % 9973:04d}"
    c.verifie(attendu in rep.get("code", "").upper().replace(" ", ""),
              "Code de contrôle du rapport mensuel",
              "Dans un Codespace ouvert sur la branche ia/rapport-mensuel, lance `python main.py rapport` : le code est sur la dernière ligne.")


def m08(c):
    a = prs_de("ia/arrondi-soldes")
    b = prs_de("ia/solde-par-categorie")
    c.verifie(any(p["merged_at"] for p in a), "`ia/arrondi-soldes` est fusionnée", "Fusionne-la en premier.")
    c.verifie(any(p["merged_at"] for p in b), "`ia/solde-par-categorie` est fusionnée après résolution du conflit",
              "Sur sa PR : Resolve conflicts, puis Mark as resolved, Commit merge, et fusionne.")
    soldes = fichier_main("tresorerie/soldes.py") or ""
    c.verifie(not any(m in soldes for m in ("<<<<<<<", "=======", ">>>>>>>")),
              "Aucun marqueur de conflit oublié dans soldes.py",
              "Les lignes <<<<<<<, ======= et >>>>>>> doivent toutes être supprimées.")
    c.verifie("rounding=ROUND_HALF_UP" in soldes and "round(total" not in soldes,
              "La bonne règle d'arrondi est conservée",
              "Garde la ligne avec ROUND_HALF_UP, supprime celle avec round(). Corrige via une nouvelle PR si besoin.")
    c.verifie("def solde_par_categorie" in soldes, "La fonction `solde_par_categorie` est conservée",
              "Pendant la résolution, seule la ligne en conflit change : le reste de la branche doit rester.")


def m09(c):
    rep = reponses()
    nettoyage = [p for p in prs_de("ia/nettoyage") if p["merged_at"]]
    c.verifie(nettoyage, "`ia/nettoyage` a été fusionnée (pour l'exercice)",
              "Ouvre une PR depuis ia/nettoyage et fusionne-la.")
    toutes = toutes_les_prs()
    c.verifie(any(annulee(p, toutes) for p in nettoyage),
              "Une pull request « Revert » a été fusionnée",
              "En bas de la PR ia/nettoyage fusionnée, clique sur Revert, puis fusionne la PR créée.")
    c.verifie((RACINE / "tests/test_categories.py").exists(), "`tests/test_categories.py` est de retour sur main")
    categories = fichier_main("tresorerie/categories.py") or ""
    c.verifie("LIDL" in categories and "SNCF" in categories, "Les mots-clés supprimés sont revenus dans categories.py")
    c.verifie("test_categories" in rep.get("fichier", ""), "Le fichier de test supprimé est identifié",
              "Dans Files changed de la PR ia/nettoyage, cherche le fichier entièrement en rouge.")


def m10(c):
    try:
        regles = gh.get(gh.repo("/rules/branches/main")) or []
    except gh.ErreurAPI:
        regles = []
    types = {r["type"] for r in regles}
    indice = "Settings › Rules › Rulesets. Une ancienne « branch protection rule » n'est pas visible pour le correcteur : utilise un ruleset."
    c.verifie("pull_request" in types, "Pull request obligatoire pour modifier main", indice)
    checks = [x.get("context") for r in regles if r["type"] == "required_status_checks"
              for x in r.get("parameters", {}).get("required_status_checks", [])]
    c.verifie("pytest" in checks, "Le check `pytest` doit être vert avant de fusionner",
              "Dans le ruleset : Require status checks to pass › Add checks › pytest.")
    if "non_fast_forward" not in types:
        c.note("Pense aussi à cocher « Block force pushes ».")


def m11(c):
    try:
        release = gh.get(gh.repo("/releases/tags/v0.1.0"))
    except gh.ErreurAPI:
        release = None
    c.verifie(release, "La release `v0.1.0` est publiée",
              "Colonne de droite : Releases › Create a new release, tag v0.1.0, puis Publish release.")
    if release and not (release.get("body") or "").strip():
        c.note("Ta release n'a pas de notes. Le bouton « Generate release notes » les écrit pour toi.")


def m12(c):
    issues = [i for i in gh.get_tout(gh.repo("/issues"), {"labels": "pour-claude", "state": "all"}) if "pull_request" not in i]
    fermees = [i for i in issues if i["state"] == "closed"]
    c.verifie(fermees, "Ton issue `pour-claude` est fermée",
              "Elle se ferme toute seule quand la PR dont la description contient « Closes #N » est fusionnée.")
    prs = [p for p in toutes_les_prs() if p["merged_at"]]
    liee = next((p for i in fermees for p in prs
                 if re.search(rf"#{i['number']}\b", (p.get("title") or "") + " " + (p.get("body") or ""))), None)
    c.verifie(liee, "Une pull request fusionnée référence cette issue",
              "Demande à Claude Code d'écrire « Closes #N » dans la description de la PR.")
    c.verifie(liee and commentaires_relecture(liee["number"]),
              "Tu as laissé au moins un commentaire de relecture sur cette PR",
              "Dans Files changed, commente au moins une ligne avant de fusionner.")
    note_squash(c, liee)


MISSIONS = {1: m01, 2: m02, 3: m03, 4: m04, 5: m05, 6: m06, 7: m07, 8: m08, 9: m09, 10: m10, 11: m11, 12: m12}


def mission_suivante(numero):
    titre = f"Mission {numero + 1:02d}"
    for i in gh.get_tout(gh.repo("/issues"), {"labels": "mission", "state": "open"}):
        if i["title"].startswith(titre):
            return i
    return None


def main():
    trouve = re.search(r"Mission (\d+)", TITRE)
    numero = int(trouve.group(1)) if trouve else 0
    c = Correction()
    if numero not in MISSIONS:
        gh.post(gh.repo(f"/issues/{NUMERO}/comments"), {"body": "Je ne reconnais pas cette mission. Ne modifie pas le titre des issues de mission."})
        return
    try:
        MISSIONS[numero](c)
    except Exception as erreur:  # le correcteur ne doit jamais rester muet
        c.verifie(False, "Le correcteur a rencontré une erreur", f"Réessaie dans une minute. Détail : `{erreur}`")

    lignes = [f"### Correction · Mission {numero:02d}", ""]
    for ok, texte, indice in c.points:
        lignes.append(f"- {'✅' if ok else '❌'} {texte}")
        if not ok and indice:
            lignes.append(f"  > Indice : {indice}")
    if c.notes:
        lignes += [""] + [f"💡 {n}" for n in c.notes]
    lignes.append("")
    if c.reussie:
        suivante = mission_suivante(numero)
        lignes.append("**Mission réussie.**" + (f" Prochaine étape : #{suivante['number']}." if suivante else " Tu as terminé l'atelier. Bravo !"))
    else:
        lignes.append("**Pas encore.** Corrige les points marqués ❌, puis commente à nouveau `/verifier`. "
                      "Les indices et la solution complète sont dans la section « Si tu bloques » de la description.")
    gh.post(gh.repo(f"/issues/{NUMERO}/comments"), {"body": "\n".join(lignes)})
    if c.reussie:
        gh.post(gh.repo(f"/issues/{NUMERO}/labels"), {"labels": ["réussie"]})
        gh.patch(gh.repo(f"/issues/{NUMERO}"), {"state": "closed", "state_reason": "completed"})
        try:
            tableau.mettre_a_jour()
        except gh.ErreurAPI as erreur:
            print(f"Tableau de bord non mis à jour : {erreur}")


if __name__ == "__main__":
    main()
