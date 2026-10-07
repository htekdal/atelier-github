titre: Mission 09 · Annuler une fusion
labels: mission, palier-4
---
> **Objectif** : enquêter sur une fusion qui a cassé quelque chose, puis l'annuler proprement.
> **Durée** : 20 minutes · **À lire avant** : carnet, section « Réparer une erreur »

## Pourquoi

Un jour, tu fusionneras une PR qui casse quelque chose. Il faut savoir revenir en arrière proprement, sans paniquer et sans réécrire l'historique.

## Étapes

- [ ] **1. Ouvrir la PR.** New pull request › `compare: ia/nettoyage` › Create pull request. Le titre est rassurant.
- [ ] **2. Fusionner sans relire.** Pour l'exercice, reproduis ton ancien réflexe : check vert › **Squash and merge**. Ne supprime pas encore la branche.
- [ ] **3. Enquêter.** Sur la PR fusionnée, onglet **Files changed**. Un fichier est entièrement rouge : lequel ? Et qu'est-ce qui a disparu dans `categories.py` ?
- [ ] **4. Mesurer les dégâts.** Les mots-clés retirés veulent dire que certaines dépenses ne sont plus catégorisées. Et le test qui l'aurait détecté a été supprimé : c'est pour ça que le check était vert.
- [ ] **5. Annuler.** En bas de l'onglet **Conversation** de la PR fusionnée, clique sur **Revert**. GitHub crée une branche et ouvre une nouvelle PR intitulée `Revert "..."`.
- [ ] **6. Relire l'annulation.** Dans **Files changed** de cette nouvelle PR : c'est l'inverse exact du diff précédent. Le fichier supprimé revient en vert.
- [ ] **7. Fusionner l'annulation.** Check vert › **Squash and merge** › Delete branch. Supprime aussi la branche `ia/nettoyage`.
- [ ] **8. Vérifier.** Onglet **Code** › `tests/` : le fichier est revenu.
- [ ] **9. Valider.** Poste le modèle ci-dessous.

## Valider

```
Fichier: 
/verifier
```

Indique le nom du fichier de test qui avait été supprimé.

## Si tu bloques

<details>
<summary>Indice 1 · Je ne trouve pas le bouton Revert</summary>

Il n'existe que sur une PR **fusionnée**, en bas de l'onglet Conversation, à côté du message « Pull request successfully merged and closed ». Si tu as fusionné en local ou si la PR n'est pas fusionnée, il n'apparaît pas.
</details>

<details>
<summary>Indice 2 · Pourquoi le check était vert ?</summary>

Un check vert signifie que les tests **restants** passent. Si une PR supprime le test qui vérifie les catégories, plus rien ne vérifie les catégories. Une PR qui supprime des tests doit toujours être justifiée.
</details>

<details>
<summary>Solution complète</summary>

Le fichier supprimé est `tests/test_categories.py`. La PR retirait aussi `LIDL`, `BOULANGERIE` et `SNCF` des mots-clés : ces dépenses tombaient dans « Autre ». Revert › fusionner la PR créée › le fichier et les mots-clés reviennent.
</details>

## Pièges fréquents

- Essayer de « réparer à la main » en recréant le fichier : Revert est plus sûr et garde l'historique propre.
- Oublier de fusionner la PR de revert : tant qu'elle n'est pas fusionnée, rien n'est annulé.

## À retenir

- **Revert** crée un nouveau commit qui fait l'inverse : l'historique garde la trace de l'erreur et de sa correction. C'est la façon sûre d'annuler quelque chose qui est déjà sur `main`.
- Méfie-toi des PR au titre vague (« nettoyage », « refactor », « améliorations ») qui suppriment des tests. Une IA peut supprimer un test qui la gêne au lieu de corriger son code.
