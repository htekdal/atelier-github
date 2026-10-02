titre: Mission 12 · Mission finale : piloter Claude Code de bout en bout
labels: mission, palier-4
---
## Pourquoi

Tu refais ta boucle habituelle avec Claude Code, mais cette fois en chef de projet : chaque étape est volontaire, et tu sais ce qui se passe à chaque instant.

## Étapes

1. Reprends l'issue `pour-claude` créée en mission 3. Note son numéro, appelons-le N.
2. Dans Claude Code, sélectionne le dépôt `atelier-github` et donne cette consigne (remplace N) :

```
Lis l'issue #N du dépôt atelier-github et implémente-la.
Travaille sur une nouvelle branche et ajoute des tests.
Ouvre ensuite une pull request vers main dont la description contient "Closes #N".
```

3. Sur GitHub, ouvre la PR. Vérifie la direction (base ← compare), les commits, et surtout **Files changed**. Reprends les critères d'acceptation de l'issue : chacun est-il rempli ?
4. Laisse au moins un commentaire de relecture sur une ligne.
5. S'il manque quelque chose, demande la correction à Claude Code en citant ton commentaire. Les nouveaux commits poussés sur la même branche mettent la PR à jour.
6. Check vert et critères remplis : **Squash and merge**, puis **Delete branch**. L'issue N se ferme toute seule grâce à « Closes #N ».

## Valider

Commente `/verifier` sur cette issue.

## À retenir

La boucle complète : issue → branche → pull request → relecture → checks → fusion → issue fermée. C'est le cœur du métier, avec ou sans IA. Applique-la telle quelle à ton appli de trésorerie.
