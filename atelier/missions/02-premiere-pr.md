titre: Mission 02 · Ta première pull request, sans terminal
labels: mission, palier-1
---
> **Objectif** : faire une fois à la main ce que Claude Code fait quand tu lui demandes « fais une PR ».
> **Durée** : 15 minutes · **À lire avant** : carnet, section « Simulateur »

## Pourquoi

Quand tu demandes à Claude Code une pull request, il enchaîne plusieurs actions : créer une branche, commiter, pousser, ouvrir la PR. Les faire une fois toi-même rend tout le reste lisible.

## Étapes

- [ ] **1. Ouvrir l'éditeur.** Onglet **Code**, clique sur `README.md`, puis sur l'icône de crayon en haut à droite du fichier (**Edit this file**).
- [ ] **2. Modifier.** Dans la section « Équipe », tout en bas, remplace `(ton pseudo ici)` par ton pseudo GitHub, par exemple `@htekdal`.
- [ ] **3. Préparer le commit.** Clique sur le bouton vert **Commit changes...** en haut à droite. Une fenêtre s'ouvre.
- [ ] **4. Choisir une branche.** Message : `docs: ajoute mon nom à l'équipe`. Puis choisis **Create a new branch for this commit and start a pull request** (pas « Commit directly to the main branch »). Nom de branche : `docs/ajout-equipe`. Clique sur **Propose changes**.
- [ ] **5. Ouvrir la PR.** GitHub affiche le formulaire de pull request. Vérifie en haut : `base: main ← compare: docs/ajout-equipe`. Clique sur **Create pull request**.
- [ ] **6. Observer.** Sur ta PR, regarde les onglets **Commits** (1 commit) et **Files changed** (ta modification en vert et rouge). En bas de l'onglet **Conversation**, le check `pytest` tourne.
- [ ] **7. Fusionner.** Quand le check est vert, clique sur la petite flèche à droite du bouton vert, choisis **Squash and merge**, puis **Confirm squash and merge**.
- [ ] **8. Nettoyer.** Clique sur **Delete branch**. La branche a rempli son rôle.
- [ ] **9. Valider.** Commente `/verifier` sur cette issue.

## Si tu bloques

<details>
<summary>Indice 1 · Je ne vois pas le crayon</summary>

Il apparaît quand tu affiches un fichier, dans la barre au-dessus de son contenu, à droite. Si tu ne le vois pas, vérifie que tu es connecté à GitHub avec le compte propriétaire du dépôt.
</details>

<details>
<summary>Indice 2 · J'ai commité directement sur main par erreur</summary>

Pas grave, mais le correcteur veut une PR. Refais une petite modification du README (par exemple ajoute « (élève ingénieur) » après ton pseudo), et cette fois choisis bien **Create a new branch for this commit and start a pull request**.
</details>

<details>
<summary>Indice 3 · Le check reste jaune ou ne démarre pas</summary>

Va dans l'onglet **Actions**. Si GitHub affiche un bandeau pour activer les workflows, accepte. Un check prend en général entre 20 secondes et une minute.
</details>

<details>
<summary>Solution complète</summary>

README.md › crayon › remplacer la ligne › Commit changes... › message › Create a new branch... › `docs/ajout-equipe` › Propose changes › Create pull request › attendre le check vert › flèche du bouton vert › Squash and merge › Confirm › Delete branch › commenter `/verifier`.
</details>

## Pièges fréquents

- Choisir « Commit directly to the main branch » : c'est exactement ce qu'on veut éviter.
- Fusionner avant que le check soit terminé. Ici, ça ne casse rien, mais prends l'habitude d'attendre.
- Oublier **Delete branch** : les vieilles branches s'accumulent et embrouillent le dépôt.

## À retenir

Tu viens de faire à la main ce que Claude Code fait pour toi : branche, commit, push, ouverture de PR. Il peut tout faire sauf une chose, qui doit rester ta décision : la fusion de l'étape 7.
