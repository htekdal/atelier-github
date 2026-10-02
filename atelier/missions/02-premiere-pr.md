titre: Mission 02 · Ta première pull request, sans terminal
labels: mission, palier-1
---
## Pourquoi

Quand tu demandes à Claude Code « fais une pull request », il enchaîne plusieurs actions : créer une branche, commiter, pousser, ouvrir la PR. Les faire une fois toi-même, à la main, rend tout le reste lisible.

## Étapes

1. Ouvre `README.md` et clique sur le crayon (**Edit this file**).
2. Dans la section « Équipe », remplace `(ton pseudo ici)` par ton pseudo GitHub.
3. Clique sur **Commit changes...**. Dans la fenêtre :
   - message : `docs: ajoute mon nom à l'équipe`
   - choisis **Create a new branch for this commit and start a pull request**
   - nom de branche : `docs/ajout-equipe`
4. Clique sur **Propose changes**, puis sur **Create pull request**.
5. Observe ta PR :
   - en haut, la direction `main ← docs/ajout-equipe` (base ← compare) ;
   - l'onglet **Files changed** : ton diff ;
   - le check `pytest` qui tourne en bas de la page.
6. Quand le check est vert, ouvre la petite flèche du bouton vert, choisis **Squash and merge**, confirme, puis clique sur **Delete branch**.

## Valider

Commente `/verifier` sur cette issue.

## À retenir

Tu viens de faire à la main ce que Claude Code fait pour toi : branche, commit, push, ouverture de PR. Il peut tout faire sauf une chose, qui doit rester ta décision : l'étape 6, la fusion.
