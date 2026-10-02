titre: Mission 08 · Résoudre un conflit
labels: mission, palier-3
---
## Pourquoi

Quand Claude Code travaille sur deux PR en parallèle, elles finissent par toucher les mêmes lignes. GitHub te demande alors de trancher. L'IA sait résoudre un conflit, mais c'est à toi de savoir quelle version est la bonne.

Deux branches modifient la même ligne de `tresorerie/soldes.py` :

- `ia/arrondi-soldes` arrondit au centime supérieur à partir d'un demi-centime, comme en comptabilité ;
- `ia/solde-par-categorie` ajoute une fonction utile, mais « simplifie » l'arrondi avec `round()`, qui transforme 0,005 € en 0,00 €.

## Étapes

1. Ouvre une PR pour chacune des deux branches.
2. Fusionne `ia/arrondi-soldes` en premier (**Squash and merge**).
3. Retourne sur la PR de `ia/solde-par-categorie`. GitHub affiche « This branch has conflicts that must be resolved ».
4. Clique sur **Resolve conflicts**. L'éditeur montre les marqueurs `<<<<<<<`, `=======` et `>>>>>>>`, avec les deux versions de la ligne.
5. Garde la ligne qui contient `ROUND_HALF_UP`, supprime l'autre, puis supprime les trois lignes de marqueurs. Ne touche pas à la nouvelle fonction `solde_par_categorie` plus bas : elle doit rester.
6. **Mark as resolved** › **Commit merge**. Attends le check, puis fusionne la PR.

## Valider

Commente `/verifier` sur cette issue.

## À retenir

Si tu gardes la mauvaise version, le test d'arrondi passe au rouge. Pendant une résolution de conflit, les tests sont ton filet de sécurité. Et quand c'est Claude qui résout, relis toujours le commit de fusion : c'est là qu'une IA peut supprimer sans bruit le travail de l'autre branche.
