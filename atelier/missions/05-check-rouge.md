titre: Mission 05 · Comprendre un check rouge
labels: mission, palier-2
---
## Pourquoi

Un check rouge n'est pas un mystère : c'est un test qui te dit précisément ce qui ne va pas. Savoir le lire te permet de donner à Claude une consigne de correction précise, au lieu de « ça ne marche pas ».

La branche `ia/prevision-90j` ajoute une prévision de trésorerie sur 90 jours.

## Étapes

1. Ouvre une pull request de `ia/prevision-90j` vers `main`.
2. Attends le check `pytest` : il passe au rouge.
3. Clique sur **Details** à côté du check. Déplie l'étape `Run pytest -v` et cherche les lignes qui commencent par `FAILED`.
4. Sous le test en échec, lis le message d'erreur : il compare la valeur **attendue** et la valeur **obtenue**.
5. Retourne sur la PR (onglet **Conversation**) et écris un commentaire comme si tu t'adressais à Claude : quel test échoue, ce qu'il attendait, ce qu'il a obtenu.
6. Ne fusionne pas. Un bouton de fusion encore cliquable ne veut pas dire que c'est une bonne idée (la mission 10 corrigera ça).

## Valider

```
Test: 
/verifier
```

Indique le nom exact du test en échec.

## Bonus

Donne ton commentaire à Claude Code et demande-lui de corriger la branche `ia/prevision-90j`. Regarde le nouveau commit apparaître dans la PR et le check repasser au vert.

## À retenir

Rouge veut dire : on ne fusionne pas. Et les logs disent toujours **quoi** : nom du test, valeur attendue, valeur obtenue. C'est exactement l'information dont l'IA a besoin pour corriger.
