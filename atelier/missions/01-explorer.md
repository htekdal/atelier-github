titre: Mission 01 · Explorer le dépôt
labels: mission, palier-1
---
## Pourquoi

Avant de confier un projet à une IA, il faut savoir s'y repérer : où est le code, ce qui a changé, quand et pourquoi. Le dépôt est une machine à remonter le temps, et tu dois savoir t'en servir.

## Étapes

1. Onglet **Code** : repère les dossiers `tresorerie/` (le code), `tests/` (les tests automatiques), `data/` (le relevé fictif) et `.github/workflows/` (les automatisations).
2. Au-dessus de la liste des fichiers, clique sur **commits** (icône d'horloge) pour voir l'historique de `main`.
3. Trouve le commit `feat: import des relevés CSV`. Note son **SHA court** : les 7 caractères affichés à droite.
4. Ouvre ce commit. Lignes vertes = ajoutées, lignes rouges = supprimées. C'est un **diff**.
5. Trouve dans quel fichier est définie la fonction `solde_courant`. Astuce : sur la page d'accueil du dépôt, appuie sur la touche `t` pour chercher un fichier, ou utilise la recherche en haut de la page.
6. Ouvre `data/exemple_releve.csv` (GitHub l'affiche sous forme de tableau) et compte les opérations.
7. Ouvre le menu des branches (le bouton `main ▾`). Les branches `ia/...` simulent le travail de Claude Code en attente de relecture. Regarde, mais ne fusionne rien pour l'instant.

## Valider

Copie ce modèle dans un commentaire de cette issue, complète-le et envoie :

```
SHA: 
Fichier: 
Operations: 
/verifier
```

## À retenir

Chaque commit a un identifiant unique (SHA), un auteur, une date et un message. Un bon message de commit te dit ce qui a changé sans ouvrir le code : c'est pour ça qu'il faut exiger de l'IA des messages clairs.
