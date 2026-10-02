titre: Mission 06 · Ce qui ne doit jamais entrer
labels: mission, palier-3
---
## Pourquoi

Une IA peut ajouter des fichiers qui n'ont rien à faire dans un dépôt : des clés d'accès, des données personnelles. Pour une appli de trésorerie, c'est le risque numéro un. Et ici, le check sera **vert** : un check vert veut dire que les tests passent, pas que la PR est sûre.

## Étapes

1. Ouvre une pull request de `ia/connexion-banque` vers `main`.
2. Dans **Files changed**, affiche la liste des fichiers (l'arborescence à gauche). Deux fichiers ne devraient jamais être versionnés. Lesquels, et pourquoi ?
3. Écris un commentaire qui explique le problème, puis clique sur **Close pull request** sans fusionner.
4. Sur la PR fermée, clique sur **Delete branch** : la branche contient encore ces fichiers.
5. Empêche que ça se reproduise : modifie `.gitignore` depuis le navigateur pour ajouter une ligne `.env`, sur une nouvelle branche avec une PR (comme en mission 2), puis fusionne-la.

## Valider

```
Fichiers: 
/verifier
```

Indique les deux fichiers, séparés par une virgule.

## À retenir

- Les clés et mots de passe vont dans un fichier `.env` listé dans `.gitignore`, ou dans **Settings › Secrets and variables** pour les automatisations.
- Les vraies données bancaires restent hors du dépôt : on versionne un exemple fictif.
- Si une vraie clé est un jour poussée, la première chose à faire est de la **révoquer** chez le fournisseur. La supprimer du code ne suffit pas : elle reste dans l'historique.
