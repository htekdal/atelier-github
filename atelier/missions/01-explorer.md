titre: Mission 01 · Explorer le dépôt
labels: mission, palier-1
---
> **Objectif** : savoir te repérer dans un dépôt : le code, l'historique, les branches.
> **Durée** : 15 minutes · **À lire avant** : carnet, sections « Git ou GitHub » et « Les quatre zones »

## Pourquoi

Avant de confier un projet à une IA, il faut savoir s'y repérer : où est le code, ce qui a changé, quand et pourquoi. Le dépôt est une machine à remonter le temps, et tu dois savoir t'en servir.

## Étapes

Coche chaque case au fur et à mesure : clique directement dessus dans cette issue. La progression s'affiche dans la liste des issues.

- [ ] **1. Repérer les dossiers.** Onglet **Code** : trouve `tresorerie/` (le code de l'appli), `tests/` (les tests automatiques), `data/` (le relevé fictif) et `.github/workflows/` (les automatisations). Clique sur chacun pour voir son contenu, puis reviens avec le nom du dépôt en haut à gauche.
- [ ] **2. Ouvrir l'historique.** Au-dessus de la liste des fichiers, à droite, clique sur **Commits** (icône d'horloge, précédée d'un nombre). Tu vois tous les commits de `main`, du plus récent au plus ancien.
- [ ] **3. Noter un SHA.** Trouve le commit `feat: import des relevés CSV`. À droite de sa ligne, le code de 7 caractères est son **SHA court**. Note-le.
- [ ] **4. Lire un diff.** Clique sur le titre de ce commit. Lignes vertes : ajoutées. Lignes rouges : supprimées. Ici, tout est vert, car le commit crée des fichiers.
- [ ] **5. Trouver une fonction.** Reviens sur la page d'accueil, appuie sur la touche `t` et tape `soldes`. Ouvre le fichier trouvé et repère `def solde_courant`.
- [ ] **6. Compter les opérations.** Ouvre `data/exemple_releve.csv`. GitHub l'affiche en tableau. Compte les opérations, sans la ligne d'en-tête.
- [ ] **7. Découvrir les branches.** Clique sur le bouton `main ▾` en haut à gauche de la liste des fichiers. Les branches `ia/...` simulent du travail de Claude Code en attente de relecture. Regarde, ne fusionne rien.
- [ ] **8. Valider.** Poste ta réponse avec le modèle ci-dessous.

## Valider

Copie ce modèle dans un commentaire de cette issue, complète-le et envoie :

```
SHA: 
Fichier: 
Operations: 
/verifier
```

Le correcteur répond en une minute environ. Tu peux le regarder travailler dans l'onglet **Actions**.

## Si tu bloques

<details>
<summary>Indice 1 · Je ne trouve pas l'historique des commits</summary>

Sur la page d'accueil du dépôt (onglet **Code**), regarde la barre grise juste au-dessus de la liste des fichiers. À droite, il y a une petite horloge suivie de « 7 Commits » (le nombre peut varier). C'est un lien.
</details>

<details>
<summary>Indice 2 · Le SHA, c'est lequel ?</summary>

Dans la liste des commits, chaque ligne a, à droite, un bouton avec un code comme `90b4ab2` et une icône de copie. C'est le SHA court. Le bouton de copie le met directement dans ton presse-papiers. Le SHA complet fait 40 caractères ; le correcteur accepte les deux.
</details>

<details>
<summary>Indice 3 · Le fichier de solde_courant</summary>

Il est dans le dossier `tresorerie/`. Son nom parle de soldes. Pour la réponse, donne le chemin, par exemple `tresorerie/nom_du_fichier.py`.
</details>

<details>
<summary>Solution complète</summary>

- SHA : celui affiché à droite de `feat: import des relevés CSV` dans l'historique.
- Fichier : `tresorerie/soldes.py`.
- Opérations : 14.
</details>

## Pièges fréquents

- Compter la ligne d'en-tête (`date;libelle;montant`) dans le nombre d'opérations.
- Prendre le SHA d'un autre commit : vérifie le message exact.
- Oublier `/verifier` dans le commentaire : sans lui, le correcteur ne se déclenche pas.

## À retenir

Chaque commit a un identifiant unique (SHA), un auteur, une date et un message. Un bon message te dit ce qui a changé sans ouvrir le code : c'est pour ça qu'il faut exiger de l'IA des messages clairs.
