titre: Mission 10 · Protéger main
labels: mission, palier-4
---
> **Objectif** : rendre impossible toute fusion sans PR et sans tests verts.
> **Durée** : 15 minutes · **À lire avant** : carnet, section « Actions et sécurité », réglages à activer

## Pourquoi

Avec une IA qui pousse vite, il faut une règle simple : rien n'entre dans `main` sans pull request et sans tests verts. GitHub peut l'imposer à tout le monde, y compris à toi et à Claude.

## Étapes

- [ ] **1. Ouvrir les réglages.** Onglet **Settings** du dépôt (tout à droite des onglets). Colonne de gauche : **Rules** › **Rulesets**.
- [ ] **2. Créer un ruleset.** **New ruleset** › **New branch ruleset**.
- [ ] **3. Le nommer et l'activer.** Ruleset name : `protection-main`. Enforcement status : passe de **Disabled** à **Active**.
- [ ] **4. Cibler main.** Section **Target branches** › **Add target** › **Include default branch**.
- [ ] **5. Exiger une PR.** Coche **Require a pull request before merging**. Laisse « Required approvals » à 0 : tu travailles seul et tu ne peux pas approuver tes propres PR.
- [ ] **6. Exiger les tests.** Coche **Require status checks to pass** › **Add checks** › tape `pytest` › sélectionne-le.
- [ ] **7. Bloquer les écrasements.** Vérifie que **Block force pushes** est coché.
- [ ] **8. Enregistrer.** Bouton **Create** tout en bas.
- [ ] **9. Tester.** Ouvre `README.md` sur main › crayon › modifie un mot › Commit changes... : l'option « Commit directly to the main branch » est maintenant refusée. Annule.
- [ ] **10. Valider.** Commente `/verifier` sur cette issue.

## Si tu bloques

<details>
<summary>Indice 1 · Je ne vois pas l'onglet Settings</summary>

Il n'apparaît que pour le propriétaire du dépôt. Vérifie que tu es connecté avec le compte qui a créé `atelier-github`. Sur un petit écran, il peut être caché dans le menu « … » à droite des onglets.
</details>

<details>
<summary>Indice 2 · pytest n'apparaît pas dans la liste des checks</summary>

GitHub propose les checks qui ont tourné récemment. Tape quand même `pytest` dans le champ : il doit apparaître. Sinon, ouvre et ferme une petite PR pour relancer un check, puis réessaie.
</details>

<details>
<summary>Indice 3 · Le correcteur dit que rien n'est protégé</summary>

Vérifie que l'Enforcement status est bien **Active** et non Disabled ou Evaluate. Le correcteur lit uniquement les rulesets : une ancienne « branch protection rule » (Settings › Branches) ne lui est pas visible.
</details>

<details>
<summary>Solution complète</summary>

Settings › Rules › Rulesets › New branch ruleset › nom `protection-main` › Active › Add target › Include default branch › Require a pull request (0 approbation) › Require status checks › pytest › Block force pushes › Create.
</details>

## Pièges fréquents

- Laisser le ruleset en Disabled : il existe mais ne protège rien.
- Exiger 1 approbation : tu bloquerais toutes tes propres PR.

## À retenir

C'est la meilleure protection contre la fusion machinale : désormais, un check rouge bloque physiquement le bouton de fusion. Fais la même chose sur le dépôt de ta vraie appli.
