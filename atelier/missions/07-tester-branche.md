titre: Mission 07 · Tester une branche avant de fusionner
labels: mission, palier-3
---
## Pourquoi

Les tests automatiques ne voient pas tout. Avant de fusionner une fonctionnalité visible, lance l'appli toi-même et regarde le résultat. **Codespaces** te donne un ordinateur complet dans le navigateur, sans rien installer.

La branche `ia/rapport-mensuel` ajoute un rapport des dépenses du mois.

## Étapes

1. Sur la page d'accueil du dépôt, ouvre le menu des branches et choisis `ia/rapport-mensuel`.
2. Bouton vert **Code** › onglet **Codespaces** › **Create codespace on ia/rapport-mensuel**. Patiente une à deux minutes : un éditeur VS Code s'ouvre dans ton navigateur.
3. En bas, dans le panneau **Terminal**, tape :

```
python main.py rapport
```

4. Lis le rapport. Les catégories te semblent-elles cohérentes avec le relevé ? Note le **code de contrôle** affiché à la dernière ligne.
5. Pour voir le dépôt depuis le terminal, tape `git status`, puis `git log --oneline -5`. Ce sont les mêmes informations que sur le site.
6. Ferme l'onglet. Sur github.com/codespaces, supprime ce codespace pour ne pas consommer ton quota gratuit.

## Valider

```
Code: 
/verifier
```

## À retenir

« Les tests passent » et « l'appli fait ce que je veux » sont deux choses différentes. Pour les fonctionnalités visibles, lance le code avant de fusionner. Codespaces, ou GitHub Desktop si tu préfères travailler sur ton ordinateur, servent à ça.
