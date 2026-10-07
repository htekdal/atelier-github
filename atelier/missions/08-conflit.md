titre: Mission 08 · Résoudre un conflit
labels: mission, palier-3
---
> **Objectif** : trancher un conflit entre deux PR depuis le site, et savoir quelle version garder.
> **Durée** : 25 minutes · **À lire avant** : carnet, section « Conflits »

## Pourquoi

Quand Claude Code travaille sur deux PR en parallèle, elles finissent par toucher les mêmes lignes. GitHub te demande alors de trancher. L'IA sait résoudre un conflit, mais c'est à toi de savoir quelle version est la bonne.

Deux branches modifient la même ligne de `tresorerie/soldes.py` :

- `ia/arrondi-soldes` arrondit au centime supérieur à partir d'un demi-centime, comme en comptabilité ;
- `ia/solde-par-categorie` ajoute une fonction utile, mais « simplifie » l'arrondi avec `round()`, qui transforme 0,005 € en 0,00 €.

## Étapes

- [ ] **1. Ouvrir les deux PR.** Une PR pour `ia/arrondi-soldes`, une autre pour `ia/solde-par-categorie`. À ce stade, aucune n'a de conflit.
- [ ] **2. Fusionner la première.** Sur la PR `ia/arrondi-soldes` : check vert › **Squash and merge** › Delete branch.
- [ ] **3. Constater le conflit.** Retourne sur la PR `ia/solde-par-categorie`. En bas : « This branch has conflicts that must be resolved ». La première fusion a modifié la ligne que cette branche modifie aussi.
- [ ] **4. Ouvrir l'éditeur.** Clique sur **Resolve conflicts**. GitHub affiche `soldes.py` avec les marqueurs `<<<<<<<`, `=======` et `>>>>>>>`.
- [ ] **5. Identifier les deux versions.** Entre `<<<<<<<` et `=======` : une version. Entre `=======` et `>>>>>>>` : l'autre. Le nom après chaque marqueur dit de quelle branche elle vient.
- [ ] **6. Choisir.** Garde la ligne qui contient `ROUND_HALF_UP`. Supprime la ligne avec `round(total, 2)`.
- [ ] **7. Effacer les marqueurs.** Supprime les trois lignes `<<<<<<< ...`, `=======` et `>>>>>>> ...`. Ne touche pas à la fonction `solde_par_categorie` plus bas.
- [ ] **8. Enregistrer.** **Mark as resolved** (en haut à droite) › **Commit merge**.
- [ ] **9. Vérifier et fusionner.** Le check se relance. Vert : **Squash and merge** › Delete branch. Rouge : lis l'indice 2.
- [ ] **10. Valider.** Commente `/verifier` sur cette issue.

## Si tu bloques

<details>
<summary>Indice 1 · À quoi doit ressembler la fonction après résolution ?</summary>

```python
def solde_courant(operations, solde_initial=Decimal("0")):
    """Solde après application de toutes les opérations."""
    total = solde_initial + sum((op.montant for op in operations), Decimal("0"))
    solde = total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return solde
```
</details>

<details>
<summary>Indice 2 · Le check est rouge après ma résolution</summary>

Ouvre les logs (**Details**). Si `test_arrondi_demi_centime_au_superieur` échoue, tu as gardé la ligne avec `round()`. Corrige `soldes.py` sur la branche `ia/solde-par-categorie` : ouvre le fichier sur cette branche, crayon, remplace la ligne, et commite directement sur cette branche. La PR se met à jour.
</details>

<details>
<summary>Indice 3 · Le bouton Resolve conflicts est grisé</summary>

GitHub ne propose l'éditeur en ligne que pour les conflits simples. Ici il doit fonctionner. Sinon, demande à Claude Code : « Sur la branche ia/solde-par-categorie, intègre main et résous le conflit dans soldes.py en gardant l'arrondi ROUND_HALF_UP. » Puis relis son commit de fusion.
</details>

<details>
<summary>Solution complète</summary>

Fusionner `ia/arrondi-soldes` › sur l'autre PR, Resolve conflicts › garder la ligne `ROUND_HALF_UP` › supprimer la ligne `round(total, 2)` et les trois marqueurs › Mark as resolved › Commit merge › attendre le check vert › Squash and merge › `/verifier`.
</details>

## Pièges fréquents

- Fusionner les PR dans l'autre ordre : le conflit apparaît alors sur `ia/arrondi-soldes`. Pas grave, garde quand même la ligne `ROUND_HALF_UP`.
- Laisser une ligne de marqueur : Python ne peut plus lire le fichier, tous les tests échouent.
- Supprimer la fonction `solde_par_categorie` en même temps que le conflit.

## À retenir

Pendant une résolution de conflit, les tests sont ton filet de sécurité : la mauvaise version fait passer le check au rouge. Et quand c'est Claude qui résout, relis toujours le commit de fusion : c'est là qu'une IA peut supprimer sans bruit le travail de l'autre branche.
