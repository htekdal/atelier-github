titre: Mission 07 · Tester une branche avant de fusionner
labels: mission, palier-3
---
> **Objectif** : lancer le code d'une branche dans le navigateur, sans rien installer.
> **Durée** : 20 minutes · **À lire avant** : carnet, section « Commandes », groupe « Inspecter »

## Pourquoi

Les tests automatiques ne voient pas tout. Avant de fusionner une fonctionnalité visible, lance l'appli toi-même et regarde le résultat. **Codespaces** te donne un ordinateur complet dans le navigateur.

La branche `ia/rapport-mensuel` ajoute un rapport des dépenses du mois.

## Étapes

- [ ] **1. Choisir la branche.** Page d'accueil du dépôt › bouton `main ▾` › choisis `ia/rapport-mensuel`. Le bouton affiche maintenant le nom de la branche.
- [ ] **2. Créer le Codespace.** Bouton vert **Code** › onglet **Codespaces** › **Create codespace on ia/rapport-mensuel**.
- [ ] **3. Patienter.** Un nouvel onglet s'ouvre. Après une à deux minutes, un éditeur VS Code apparaît, avec un panneau **Terminal** en bas.
- [ ] **4. Vérifier la branche.** Dans le terminal, tape `git status`. La première ligne doit dire `On branch ia/rapport-mensuel`.
- [ ] **5. Lancer l'appli.** Tape `python main.py rapport` puis Entrée.
- [ ] **6. Lire le résultat.** Les catégories te semblent-elles cohérentes avec le relevé ? Note le **code de contrôle** affiché à la dernière ligne.
- [ ] **7. Explorer.** Tape `git log --oneline -5` : les mêmes commits que sur le site, vus depuis le terminal.
- [ ] **8. Éteindre.** Ferme l'onglet. Va sur github.com/codespaces, clique sur les **…** à droite de ton codespace › **Delete**.
- [ ] **9. Valider.** Poste le modèle ci-dessous.

## Valider

```
Code: 
/verifier
```

## Si tu bloques

<details>
<summary>Indice 1 · « Commande inconnue : rapport »</summary>

Ton Codespace est ouvert sur `main`, qui ne contient pas encore le rapport. Dans le terminal, tape `git switch ia/rapport-mensuel`, puis relance `python main.py rapport`. C'est exactement ce que fait Claude Code quand il change de branche.
</details>

<details>
<summary>Indice 2 · Je ne vois pas le terminal</summary>

Menu en haut à gauche (les trois traits) › **Terminal** › **New Terminal**. Ou le raccourci Ctrl + ` (accent grave).
</details>

<details>
<summary>Indice 3 · « python: command not found »</summary>

Essaie `python3 main.py rapport`. Le Codespace par défaut contient Python ; selon l'image, la commande s'appelle `python` ou `python3`.
</details>

<details>
<summary>Solution complète</summary>

Code › Codespaces › Create codespace on ia/rapport-mensuel › terminal › `git status` › `python main.py rapport` › recopier la ligne « Code de contrôle : RM-xxxx » dans le modèle › supprimer le codespace. Le code commence par `RM-` suivi de 4 chiffres.
</details>

## Pièges fréquents

- Créer le Codespace sur `main` au lieu de la branche (voir indice 1).
- Oublier de supprimer le codespace : il consomme ton quota gratuit mensuel tant qu'il existe.

## À retenir

« Les tests passent » et « l'appli fait ce que je veux » sont deux choses différentes. Pour les fonctionnalités visibles, lance le code avant de fusionner. Codespaces, ou GitHub Desktop si tu préfères travailler sur ton ordinateur, servent à ça.
