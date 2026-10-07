titre: Mission 04 · Relire la pull request de l'IA
labels: mission, palier-2
---
> **Objectif** : relire une PR avant de la fusionner, au lieu de cliquer machinalement.
> **Durée** : 20 minutes · **À lire avant** : carnet, section « Anatomie d'une PR »

## Pourquoi

Jusqu'ici, tu fusionnais les PR de Claude Code un peu machinalement. Ici, tu apprends à lire ce que l'IA propose avant de dire oui. La branche `ia/export-csv` contient son travail : un export CSV des totaux par catégorie.

## Étapes

- [ ] **1. Ouvrir la PR.** Onglet **Pull requests** › **New pull request**. Laisse `base: main`, choisis `compare: ia/export-csv`. Clique sur **Create pull request**, titre : « Export CSV des totaux par catégorie », puis **Create pull request** à nouveau.
- [ ] **2. Lire les commits.** Onglet **Commits** : combien de commits ? Les messages racontent-ils une progression logique (code, tests, branchement dans `main.py`) ?
- [ ] **3. Lire le diff.** Onglet **Files changed**. Pour chaque fichier, réponds à trois questions : qu'est-ce qui est ajouté, où, et est-ce cohérent avec le titre ? Pas besoin de comprendre chaque ligne de Python.
- [ ] **4. Vérifier les tests.** Y a-t-il un fichier dans `tests/` ? Une fonctionnalité sans test est un signal d'alerte.
- [ ] **5. Commenter une ligne.** Survole une ligne : un **+** bleu apparaît à gauche. Clique, écris une question de relecteur (exemple : « Que se passe-t-il si le relevé est vide ? »), puis **Start a review**.
- [ ] **6. Terminer la relecture.** En haut à droite, bouton **Review changes** (ou **Finish your review**) › choisis **Comment** › **Submit review**.
- [ ] **7. Constater.** **Approve** est grisé : GitHub interdit d'approuver sa propre PR. Si Claude Code ouvre ses PR avec ton compte, c'est ton cas : la relecture repose entièrement sur toi.
- [ ] **8. Fusionner.** Check `pytest` vert : flèche du bouton vert › **Squash and merge** › **Confirm**, puis **Delete branch**.
- [ ] **9. Valider.** Commente `/verifier` sur cette issue.

## Si tu bloques

<details>
<summary>Indice 1 · Je ne trouve pas la branche ia/export-csv dans « compare »</summary>

Clique sur le menu `compare: main ▾` et tape `export` dans la recherche du menu. Si elle n'apparaît pas, tu l'as peut-être supprimée : onglet **Code** › menu des branches › **View all branches** pour vérifier.
</details>

<details>
<summary>Indice 2 · Le + bleu n'apparaît pas</summary>

Il n'apparaît que dans l'onglet **Files changed**, quand la souris est sur le numéro de ligne ou juste à côté. Sur téléphone, utilise plutôt un ordinateur pour cette mission.
</details>

<details>
<summary>Indice 3 · Le correcteur ne voit pas mon commentaire</summary>

Il doit être posé **sur une ligne** du diff (onglet Files changed). Un commentaire dans l'onglet Conversation ne compte pas ici. Et vérifie que ta revue est bien soumise : tant que tu n'as pas cliqué sur **Submit review**, tes commentaires restent « Pending », visibles de toi seul.
</details>

<details>
<summary>Solution complète</summary>

New pull request › compare `ia/export-csv` › Create › Files changed › + sur une ligne › question › Start a review › Review changes › Comment › Submit review › attendre le check vert › Squash and merge › Confirm › Delete branch › `/verifier`.
</details>

## Pièges fréquents

- Laisser une revue en « Pending » : tes commentaires n'existent pas pour les autres.
- Juger la PR sur sa description ou son titre au lieu du diff.
- Fusionner avec « Create a merge commit » : pas faux, mais en solo préfère « Squash and merge ».

## À retenir

**Files changed** est l'onglet le plus important de GitHub pour toi. Une PR se juge sur son diff, jamais sur sa description : une IA peut décrire avec assurance un code qui ne fait pas ce qu'elle annonce.
