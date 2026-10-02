titre: Mission 10 · Protéger main
labels: mission, palier-4
---
## Pourquoi

Avec une IA qui pousse vite, il faut une règle simple : rien n'entre dans `main` sans pull request et sans tests verts. GitHub peut l'imposer à tout le monde, y compris à toi et à Claude.

## Étapes

1. Onglet **Settings** › dans la colonne de gauche, **Rules** › **Rulesets** › **New ruleset** › **New branch ruleset**.
2. **Ruleset name** : `protection-main`. **Enforcement status** : **Active**.
3. **Target branches** › **Add target** › **Include default branch**.
4. Coche **Require a pull request before merging**. Laisse le nombre d'approbations requises à 0 : tu travailles seul et tu ne peux pas approuver tes propres PR.
5. Coche **Require status checks to pass** › **Add checks** › choisis `pytest`.
6. Vérifie que **Block force pushes** est coché. Clique sur **Create**.
7. Test : essaie de modifier `README.md` directement sur `main` depuis le navigateur. GitHub t'oblige à passer par une branche.

## Valider

Commente `/verifier` sur cette issue.

## À retenir

C'est la meilleure protection contre la fusion machinale : désormais, un check rouge bloque physiquement le bouton de fusion. Fais la même chose sur le dépôt de ta vraie appli.
