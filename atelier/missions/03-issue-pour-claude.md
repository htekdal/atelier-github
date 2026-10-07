titre: Mission 03 · Rédiger une issue qui sert de prompt
labels: mission, palier-2
---
> **Objectif** : écrire un cahier des charges que Claude Code peut exécuter et que tu peux vérifier.
> **Durée** : 15 minutes · **À lire avant** : carnet, section « Le cycle quotidien », partie « Ta boucle avec Claude Code »

## Pourquoi

Une issue bien rédigée, c'est un prompt que Claude Code peut lire directement, et une trace durable : dans six mois, tu sauras pourquoi telle fonctionnalité existe. Ses critères d'acceptation te serviront ensuite à juger objectivement la PR de l'IA.

## Étapes

- [ ] **1. Choisir le besoin.** Par défaut : afficher une alerte quand le solde passe sous 100 €. Tu peux choisir une autre amélioration de l'appli si tu préfères.
- [ ] **2. Créer l'issue.** Onglet **Issues** › bouton vert **New issue** (choisis « Blank issue » si GitHub propose des modèles).
- [ ] **3. Titre.** Court et concret : `Alerte quand le solde passe sous 100 €`.
- [ ] **4. Corps.** Copie ce squelette et remplis chaque partie :

```
## Contexte
Pourquoi ce besoin existe.

## Objectif
Ce que l'appli doit faire, vu par l'utilisateur.

## Critères d'acceptation
- [ ] un critère vérifiable
- [ ] un autre critère vérifiable
```

- [ ] **5. Écrire de bons critères.** Chacun doit pouvoir se vérifier par oui ou par non en lançant l'appli ou en lisant le code.
- [ ] **6. Ajouter le label.** Dans la colonne de droite, **Labels** › coche `pour-claude`.
- [ ] **7. Créer.** Clique sur **Create**. Note le numéro de ton issue (#...) : tu la confieras à Claude Code dans la mission 12.
- [ ] **8. Valider.** Reviens sur **cette** issue (la mission) et commente `/verifier`.

## Si tu bloques

<details>
<summary>Indice 1 · À quoi ressemble un bon critère ?</summary>

Bon : « `python main.py` affiche une ligne commençant par ATTENTION si le solde final est inférieur à 100,00 € ».
Bon : « Un test vérifie le cas d'un solde à 99,99 € et le cas d'un solde à 100,00 € ».
Mauvais : « l'alerte marche bien ». Mauvais : « le code est propre ».
</details>

<details>
<summary>Indice 2 · Le correcteur ne trouve pas mes sections</summary>

Les titres doivent être exactement `## Contexte`, `## Objectif` et `## Critères d'acceptation`, avec les deux dièses et un espace. Il faut au moins deux lignes commençant par `- [ ]`.
</details>

<details>
<summary>Solution complète (exemple)</summary>

```
## Contexte
Je veux être prévenu avant d'être à découvert.

## Objectif
Après le résumé, l'appli affiche une alerte si le solde final est sous un seuil de 100 €.

## Critères d'acceptation
- [ ] `python main.py` affiche « ATTENTION : solde sous 100,00 € » quand le solde final est inférieur à 100 €
- [ ] Rien n'est affiché quand le solde est supérieur ou égal à 100 €
- [ ] Le seuil est une constante facile à modifier
- [ ] Des tests couvrent les cas 99,99 € et 100,00 €
```
</details>

## Pièges fréquents

- Oublier le label `pour-claude`, ou créer un nouveau label au nom proche.
- Commenter `/verifier` sur ta nouvelle issue au lieu de l'issue de mission.
- Écrire des critères vagues : tu ne pourras pas juger la PR de l'IA objectivement.

## À retenir

Les cases `- [ ]` deviennent de vraies cases à cocher sur GitHub. Quand la PR de l'IA arrive, tu les coches une par une en vérifiant le diff : c'est ta grille de correction.
