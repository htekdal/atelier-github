titre: Mission 04 · Relire la pull request de l'IA
labels: mission, palier-2
---
## Pourquoi

Jusqu'ici, tu fusionnais les PR de Claude Code un peu machinalement. Ici, tu apprends à lire ce que l'IA propose avant de dire oui. La branche `ia/export-csv` contient son travail : un export CSV des totaux par catégorie.

## Étapes

1. Onglet **Pull requests** › **New pull request**. Choisis `base: main` et `compare: ia/export-csv`, puis **Create pull request**. Donne-lui un titre clair, par exemple « Export CSV des totaux par catégorie ».
2. Onglet **Commits** : combien de commits ? Que raconte chaque message ?
3. Onglet **Files changed** : lis chaque fichier. Pas besoin de tout comprendre en Python. Demande-toi : qu'est-ce qui est ajouté, où, et est-ce que ça correspond au titre ? Y a-t-il des tests ?
4. Survole une ligne et clique sur le **+** bleu qui apparaît à gauche. Écris une question de relecteur, par exemple « Que se passe-t-il si le relevé est vide ? ». Clique sur **Start a review**.
5. En haut à droite, **Finish your review** (ou **Review changes**) › choisis **Comment** › **Submit review**.
6. Remarque que **Approve** est grisé : GitHub interdit d'approuver sa propre PR. Si Claude Code ouvre ses PR avec ton compte, elles sont à ton nom, et la relecture repose entièrement sur toi.
7. Check `pytest` vert ? **Squash and merge**, puis **Delete branch**.

## Valider

Commente `/verifier` sur cette issue.

## À retenir

**Files changed** est l'onglet le plus important de GitHub pour toi. Une PR se juge sur son diff, jamais sur sa description : une IA peut décrire avec assurance un code qui ne fait pas ce qu'elle annonce.
