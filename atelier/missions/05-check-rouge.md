titre: Mission 05 · Comprendre un check rouge
labels: mission, palier-2
---
> **Objectif** : lire les logs d'un test en échec et formuler une consigne de correction précise.
> **Durée** : 15 minutes · **À lire avant** : carnet, section « Actions et sécurité », début

## Pourquoi

Un check rouge n'est pas un mystère : c'est un test qui te dit précisément ce qui ne va pas. Savoir le lire te permet de donner à Claude une consigne de correction précise, au lieu de « ça ne marche pas ».

La branche `ia/prevision-90j` ajoute une prévision de trésorerie sur 90 jours.

## Étapes

- [ ] **1. Ouvrir la PR.** Pull requests › New pull request › `compare: ia/prevision-90j` › Create pull request.
- [ ] **2. Attendre le verdict.** En bas de l'onglet **Conversation**, le check `pytest` passe au rouge (croix rouge, « Some checks were not successful »).
- [ ] **3. Ouvrir les logs.** Clique sur **Details** à droite du check `pytest`. Tu arrives sur la page du job.
- [ ] **4. Trouver l'échec.** Déplie l'étape **Run pytest -v**. Fais défiler jusqu'aux lignes `FAILED`. Note le nom du test, après les `::`.
- [ ] **5. Comprendre l'erreur.** Remonte au bloc de ce test, juste au-dessus, dans la partie `FAILURES`. Repère la ligne `assert` et les lignes `E` : elles montrent la valeur **attendue** et la valeur **obtenue**.
- [ ] **6. Écrire à Claude.** Retourne sur la PR, onglet **Conversation**, et écris en bas un commentaire précis : quel test échoue, ce qu'il attendait, ce qu'il a obtenu, et ta supposition sur la cause. Clique sur **Comment**.
- [ ] **7. Ne pas fusionner.** Laisse la PR ouverte. Le bouton de fusion est encore cliquable : la mission 10 corrigera ça.
- [ ] **8. Valider.** Poste le modèle ci-dessous sur cette issue.

## Valider

```
Test: 
/verifier
```

## Si tu bloques

<details>
<summary>Indice 1 · Je ne trouve pas le bouton Details</summary>

Dans la PR, onglet **Conversation**, descends jusqu'à l'encadré des checks, juste au-dessus du bouton de fusion. Si l'encadré est replié, clique sur **Show all checks**. Autre chemin : l'onglet **Checks** de la PR.
</details>

<details>
<summary>Indice 2 · Comment lire une ligne FAILED</summary>

Exemple de format : `FAILED tests/test_fichier.py::nom_du_test - AssertionError`. Le nom du test est la partie entre `::` et ` - `. C'est ce nom que le correcteur attend.
</details>

<details>
<summary>Indice 3 · Un exemple de bon commentaire</summary>

« Le test X échoue : il attend 90 jours dans la période du 01/10 au 29/12, mais la fonction `periode` en renvoie 89. Le dernier jour semble exclu. Peux-tu corriger `periode` pour inclure la date de fin ? »
</details>

<details>
<summary>Solution complète</summary>

Le test en échec est `test_prevision_inclut_le_dernier_jour`. La fonction `periode` utilise `range((fin - debut).days)`, qui s'arrête un jour trop tôt : il faudrait `+ 1`. Ton rôle n'est pas de corriger le code, mais de décrire le problème assez précisément pour que Claude le corrige du premier coup.
</details>

## Bonus

Donne ton commentaire à Claude Code et demande-lui de corriger la branche `ia/prevision-90j`. Regarde le nouveau commit apparaître dans la PR et le check repasser au vert.

## Pièges fréquents

- Fusionner par réflexe. Si c'est fait, la mission 9 t'apprendra à annuler, et le correcteur acceptera une fusion annulée.
- Recopier toute la sortie des logs : le nom du test suffit pour la validation.

## À retenir

Rouge veut dire : on ne fusionne pas. Et les logs disent toujours **quoi** : nom du test, valeur attendue, valeur obtenue. C'est exactement l'information dont l'IA a besoin pour corriger.
