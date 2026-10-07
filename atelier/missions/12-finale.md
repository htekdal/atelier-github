titre: Mission 12 · Mission finale : piloter Claude Code de bout en bout
labels: mission, palier-4
---
> **Objectif** : refaire ta boucle habituelle avec Claude Code, en chef de projet.
> **Durée** : 30 à 45 minutes · **À relire avant** : carnet, « Ta boucle avec Claude Code »

## Pourquoi

Tu refais ce que tu faisais déjà, mais cette fois chaque étape est volontaire, et tu sais ce qui se passe à chaque instant.

## Étapes

- [ ] **1. Reprendre l'issue.** Ouvre l'issue `pour-claude` de la mission 3. Note son numéro N et relis ses critères d'acceptation.
- [ ] **2. Briefer Claude Code.** Dans Claude Code, sélectionne le dépôt `atelier-github` et donne cette consigne (remplace N) :

```
Lis l'issue #N du dépôt atelier-github et implémente-la.
Travaille sur une nouvelle branche et ajoute des tests.
Ouvre ensuite une pull request vers main dont la description contient "Closes #N".
```

- [ ] **3. Ouvrir la PR sur GitHub.** Onglet **Pull requests** : la PR de Claude apparaît. Vérifie la direction (`main ←` sa branche) et que la description contient `Closes #N`.
- [ ] **4. Lire les commits.** Onglet **Commits** : les messages sont-ils clairs ?
- [ ] **5. Relire le diff.** Onglet **Files changed** : aucun fichier inattendu, aucun secret, aucun test supprimé. Des tests ajoutés ?
- [ ] **6. Cocher les critères.** Dans ton issue N, coche chaque critère d'acceptation que tu as vérifié dans le diff.
- [ ] **7. Commenter.** Laisse au moins un commentaire sur une ligne du diff, puis **Submit review**.
- [ ] **8. Faire corriger si besoin.** S'il manque quelque chose, demande la correction à Claude Code en citant ton commentaire. Ses nouveaux commits mettent la PR à jour.
- [ ] **9. Tester si c'est visible.** Pour une fonctionnalité qui s'affiche, lance-la dans un Codespace sur sa branche (comme en mission 7).
- [ ] **10. Fusionner.** Check vert et critères cochés : **Squash and merge** › **Delete branch**. L'issue N se ferme toute seule.
- [ ] **11. Valider.** Commente `/verifier` sur cette issue.

## Si tu bloques

<details>
<summary>Indice 1 · Claude n'a pas mis « Closes #N »</summary>

Sur la PR, à droite du premier message (la description), clique sur **…** › **Edit**, ajoute `Closes #N` sur une ligne, puis **Update comment**. Ça marche même après la fusion pour le correcteur, mais l'issue ne se fermera alors pas toute seule : ferme-la à la main.
</details>

<details>
<summary>Indice 2 · Le check est rouge sur la PR de Claude</summary>

Applique la mission 5 : Details › Run pytest -v › ligne FAILED › renvoie à Claude le nom du test, l'attendu et l'obtenu. Avec le ruleset de la mission 10, tu ne pourras de toute façon pas fusionner.
</details>

<details>
<summary>Indice 3 · Claude Code ne voit pas le dépôt</summary>

Le dépôt doit être accessible à Claude Code via ta connexion GitHub. Vérifie dans les réglages de Claude Code que `atelier-github` fait partie des dépôts autorisés.
</details>

<details>
<summary>Solution complète</summary>

Issue N › consigne à Claude Code › PR ouverte avec « Closes #N » › relecture des commits et de Files changed › critères cochés dans l'issue › au moins un commentaire de ligne soumis › corrections éventuelles › check vert › Squash and merge › Delete branch › issue N fermée › `/verifier`.
</details>

## Pièges fréquents

- Fusionner dès que Claude annonce « c'est fait », sans ouvrir Files changed.
- Accepter une PR qui touche des fichiers sans rapport avec l'issue : demande à Claude de les retirer.

## À retenir

La boucle complète : issue → branche → pull request → relecture → checks → fusion → issue fermée. C'est le cœur du métier, avec ou sans IA. Applique-la telle quelle à ton appli de trésorerie.
