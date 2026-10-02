"""Petit client pour l'API REST de GitHub, sans dépendance externe."""
import json
import os
import urllib.error
import urllib.parse
import urllib.request

API = os.environ.get("GITHUB_API_URL", "https://api.github.com")
REPO = os.environ.get("GITHUB_REPOSITORY", "")
TOKEN = os.environ.get("GH_TOKEN", "")


class ErreurAPI(Exception):
    def __init__(self, statut, message):
        super().__init__(f"{statut}: {message}")
        self.statut = statut


def requete(methode, chemin, donnees=None, params=None):
    url = chemin if chemin.startswith("http") else f"{API}{chemin}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    corps = json.dumps(donnees).encode() if donnees is not None else None
    req = urllib.request.Request(url, data=corps, method=methode)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    if corps is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req) as reponse:
            texte = reponse.read().decode()
            lien = reponse.headers.get("Link", "")
            return (json.loads(texte) if texte else None), lien
    except urllib.error.HTTPError as erreur:
        raise ErreurAPI(erreur.code, erreur.read().decode()[:300]) from None


def get(chemin, params=None):
    return requete("GET", chemin, params=params)[0]


def get_tout(chemin, params=None):
    """GET paginé : renvoie la liste complète (10 pages de 100 au maximum)."""
    params = dict(params or {}, per_page=100)
    resultats, url = [], chemin
    for _ in range(10):
        donnees, lien = requete("GET", url, params=params)
        resultats.extend(donnees)
        suivant = [p for p in lien.split(",") if 'rel="next"' in p]
        if not suivant:
            break
        url, params = suivant[0].split(";")[0].strip(" <>"), None
    return resultats


def post(chemin, donnees):
    return requete("POST", chemin, donnees)[0]


def patch(chemin, donnees):
    return requete("PATCH", chemin, donnees)[0]


def repo(chemin=""):
    return f"/repos/{REPO}{chemin}"
