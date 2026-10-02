titre: Mission 09 · Annuler une fusion
labels: mission, palier-4
---
## Pourquoi

Un jour, tu fusionneras une PR qui casse quelque chose. Il faut savoir revenir en arrière proprement, sans paniquer et sans réécrire l'historique.

## Étapes

1. Ouvre une PR de `ia/nettoyage` vers `main`. Son titre est rassurant, le check est vert. Pour l'exercice, fusionne-la **sans relire**, comme avant.
2. Maintenant, enquête. Sur la PR fusionnée, ouvre **Files changed**. Qu'est-ce qui a disparu ? Qu'est-ce qui a changé dans les catégories ?
3. Indice : un check vert signifie que les tests **restants** passent. Il ne dit rien des tests qui ont été supprimés.
4. En bas de la PR fusionnée, clique sur **Revert**. GitHub crée une nouvelle PR qui annule exactement ces changements. Ouvre-la, regarde son diff (l'inverse du précédent), puis fusionne-la.
5. Vérifie dans l'onglet **Code** que le fichier supprimé est revenu.

## Valider

```
Fichier: 
/verifier
```

Indique le nom du fichier de test qui avait été supprimé.

## À retenir

- **Revert** crée un nouveau commit qui fait l'inverse : l'historique garde la trace de l'erreur et de sa correction. C'est la façon sûre d'annuler quelque chose qui est déjà sur `main`.
- Méfie-toi des PR au titre vague (« nettoyage », « refactor », « améliorations ») qui suppriment des tests. Une IA peut supprimer un test qui la gêne au lieu de corriger son code.
