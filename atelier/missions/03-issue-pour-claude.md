titre: Mission 03 · Rédiger une issue qui sert de prompt
labels: mission, palier-2
---
## Pourquoi

Une issue bien rédigée, c'est un cahier des charges que Claude Code peut lire directement, et une trace durable : dans six mois, tu sauras pourquoi telle fonctionnalité existe. Les critères d'acceptation te serviront ensuite à juger objectivement la PR de l'IA.

## Étapes

1. Onglet **Issues** › **New issue**.
2. Titre : `Alerte quand le solde passe sous 100 €` (ou une autre amélioration de l'appli qui te plaît).
3. Dans le corps, utilise ces trois titres, exactement :

```
## Contexte
Pourquoi ce besoin existe.

## Objectif
Ce que l'appli doit faire, vu par l'utilisateur.

## Critères d'acceptation
- [ ] un critère vérifiable
- [ ] un autre critère vérifiable
```

4. Dans la colonne de droite, **Labels** › ajoute `pour-claude`.
5. Clique sur **Create** et note le numéro de l'issue (#...). Tu la confieras à Claude Code dans la mission 12.

Exemple de bon critère : « `python main.py` affiche ATTENTION si le solde final est inférieur à 100,00 € ». Exemple de mauvais critère : « l'alerte marche bien ».

## Valider

Commente `/verifier` sur cette issue (celle de la mission, pas la tienne).

## À retenir

Les cases `- [ ]` deviennent de vraies cases à cocher sur GitHub. Quand la PR de l'IA arrive, tu les coches une par une en vérifiant le diff : c'est ta grille de correction.
