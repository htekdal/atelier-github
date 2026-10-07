titre: Mission 06 · Ce qui ne doit jamais entrer
labels: mission, palier-3
---
> **Objectif** : repérer dans une PR les fichiers qui ne doivent jamais être versionnés, même quand le check est vert.
> **Durée** : 20 minutes · **À lire avant** : carnet, section « Actions et sécurité », partie sécurité

## Pourquoi

Une IA peut ajouter des fichiers qui n'ont rien à faire dans un dépôt : des clés d'accès, des données personnelles. Pour une appli de trésorerie, c'est le risque numéro un. Et ici, le check sera **vert** : un check vert veut dire que les tests passent, pas que la PR est sûre.

## Étapes

- [ ] **1. Ouvrir la PR.** Pull requests › New pull request › `compare: ia/connexion-banque` › Create pull request.
- [ ] **2. Regarder la liste des fichiers.** Onglet **Files changed**. À gauche, l'arborescence liste tous les fichiers touchés (si elle est masquée, clique sur l'icône d'arborescence en haut à gauche du diff).
- [ ] **3. Inspecter chaque fichier.** Pour chacun, demande-toi : contient-il du code, un secret, ou des données personnelles ?
- [ ] **4. Identifier les deux intrus.** Deux fichiers ne doivent jamais être versionnés. Note leurs noms.
- [ ] **5. Expliquer.** Onglet **Conversation** : écris un commentaire qui dit quels fichiers posent problème et pourquoi.
- [ ] **6. Fermer sans fusionner.** Bouton **Close pull request**, sous la zone de commentaire.
- [ ] **7. Supprimer la branche.** Sur la PR fermée, clique sur **Delete branch** : la branche contient encore ces fichiers.
- [ ] **8. Prévenir la suite.** Ouvre `.gitignore` sur main › crayon › ajoute une ligne `.env` à la fin › **Commit changes...** › **Create a new branch...** › Propose changes › Create pull request › fusionne quand le check est vert.
- [ ] **9. Valider.** Poste le modèle ci-dessous.

## Valider

```
Fichiers: 
/verifier
```

Indique les deux fichiers, séparés par une virgule.

## Si tu bloques

<details>
<summary>Indice 1 · Quels types de fichiers chercher ?</summary>

Un fichier dont le nom commence par un point et qui contient une ligne `NOM=valeur` : c'est souvent un fichier de configuration avec des secrets. Et un fichier de données dont le nom suggère qu'il s'agit de vraies données, avec des noms de personnes et des adresses.
</details>

<details>
<summary>Indice 2 · Pourquoi le check est vert alors ?</summary>

Les tests vérifient que le code fonctionne. Aucun test ne vérifie qu'un fichier de secrets est absent. C'est ton travail de relecteur, aidé par la « push protection » de GitHub pour les clés de services connus.
</details>

<details>
<summary>Solution complète</summary>

Les intrus sont `.env` (il contient une clé d'API, fausse ici) et `data/releve_reel_septembre.csv` (des données bancaires « réelles » avec noms et adresse). Le code de `tresorerie/banque.py` et son test sont corrects : la bonne réponse aurait été de demander à Claude de retirer ces deux fichiers de la branche. Pour l'exercice, on ferme la PR.
</details>

## Pièges fréquents

- Fusionner parce que le check est vert. Si c'est fait, utilise **Revert** sur la PR (voir mission 9) : le correcteur accepte une fusion annulée.
- Fermer la PR sans supprimer la branche : les fichiers restent accessibles dans le dépôt.
- Modifier `.gitignore` directement sur main : passe par une PR, c'est l'habitude à prendre.

## À retenir

- Les clés vont dans un fichier `.env` listé dans `.gitignore`, ou dans **Settings › Secrets and variables** pour les automatisations.
- Les vraies données bancaires restent hors du dépôt : on versionne un exemple fictif.
- Si une vraie clé est un jour poussée, la première chose à faire est de la **révoquer** chez le fournisseur. La supprimer du code ne suffit pas : elle reste dans l'historique.
