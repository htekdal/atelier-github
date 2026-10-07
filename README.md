# Atelier GitHub

Un dépôt d'entraînement pour apprendre à piloter un projet sur GitHub quand c'est une IA (Claude Code) qui écrit le code.

Tu ne codes pas. Tu explores, tu rédiges les demandes, tu relis, tu décides, tu répares. Bref, tu fais le travail d'un chef de projet technique.

## Démarrer (mission 0)

1. Ouvre l'onglet **Actions**. Si GitHub demande d'activer les workflows, accepte.
2. Dans la colonne de gauche, clique sur **Démarrer l'atelier**, puis **Run workflow** › **Run workflow**.
3. Patiente une minute. L'onglet **Issues** contient alors 12 missions et un **Tableau de bord**.
4. Ouvre le tableau de bord et épingle-le : colonne de droite › **Pin issue**. Puis commence par la mission 01.

Si tu as déjà lancé « Démarrer l'atelier » avant une mise à jour de l'atelier, relance-le : les missions non commencées prennent leur nouvelle version, ta progression est conservée.

## Comment ça marche

- **Chaque mission est une issue** : objectif, durée, étapes à cocher, indices progressifs, solution complète, pièges fréquents et ce qu'il faut retenir.
- **Coche les étapes directement dans l'issue.** La progression (par exemple « 3 of 8 tasks ») s'affiche dans la liste des issues.
- **Bloqué ?** Ouvre la section « Si tu bloques » : les indices sont repliés du plus léger au plus précis, puis la solution. Essaie d'abord sans.
- **Le tableau de bord** se coche tout seul à chaque mission validée.
- **Quand tu as fini, commente `/verifier`** sur l'issue de la mission. Un correcteur automatique (un workflow GitHub Actions) examine l'état du dépôt et te répond en commentaire, en une minute environ. Si tout est bon, il ferme l'issue. Sinon, il te dit ce qui manque.
- **Les branches `ia/...` simulent le travail de Claude Code.** Chacune contient une fonctionnalité en attente de relecture, avec ses qualités et ses pièges. Ne les fusionne que lorsqu'une mission te le demande.
- Tu peux suivre le correcteur en direct dans l'onglet **Actions**.

## Les quatre paliers

| Palier | Thème | Missions |
|---|---|---|
| 1 | Lire et naviguer | 01 Explorer le dépôt · 02 Ta première pull request |
| 2 | Piloter l'IA | 03 Rédiger une issue · 04 Relire une PR · 05 Comprendre un check rouge |
| 3 | Contrôler | 06 Ce qui ne doit jamais entrer · 07 Tester une branche · 08 Résoudre un conflit |
| 4 | Réparer et protéger | 09 Annuler une fusion · 10 Protéger main · 11 Publier une version · 12 Mission finale avec Claude Code |

## L'appli

Une mini appli de trésorerie en Python : elle importe un relevé bancaire **fictif**, catégorise les dépenses et calcule le solde.

```
python main.py
```

```
.
├── main.py                  point d'entrée
├── tresorerie/              le code de l'appli
│   ├── import_csv.py        lecture des relevés
│   ├── soldes.py            calcul et affichage des soldes
│   └── categories.py        catégorisation des dépenses
├── tests/                   tests automatiques (pytest)
├── data/exemple_releve.csv  relevé fictif de septembre 2026
├── atelier/                 missions et correcteur (ne pas modifier)
└── .github/workflows/       automatisations GitHub Actions
```

## Équipe

- Atelier préparé avec Claude
- (ton pseudo ici)
