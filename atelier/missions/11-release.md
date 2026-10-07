titre: Mission 11 · Publier une version
labels: mission, palier-4
---
> **Objectif** : figer un état stable de l'appli sous un numéro de version.
> **Durée** : 10 minutes · **À lire avant** : carnet, glossaire, termes « Tag » et « Release »

## Pourquoi

Une release fige un état stable de ton appli, avec un nom (`v0.1.0`) et des notes. Si une future PR de l'IA casse tout, tu sais exactement vers quelle version revenir, et ce qu'elle contenait.

## Étapes

- [ ] **1. Vérifier main.** Onglet **Code** : le dernier check de main est vert (coche verte à côté du dernier commit).
- [ ] **2. Ouvrir les releases.** Colonne de droite de la page d'accueil : **Releases** › **Create a new release** (ou **Draft a new release**).
- [ ] **3. Créer le tag.** **Choose a tag** › tape `v0.1.0` › clique sur **Create new tag: v0.1.0 on publish**. Target : `main`.
- [ ] **4. Titrer.** Release title : `v0.1.0 · Première version stable`.
- [ ] **5. Générer les notes.** Clique sur **Generate release notes**. GitHub liste automatiquement les PR fusionnées. Relis-les : c'est le journal de ton projet.
- [ ] **6. Publier.** Laisse « Set as the latest release » coché › **Publish release**.
- [ ] **7. Valider.** Commente `/verifier` sur cette issue.

## Si tu bloques

<details>
<summary>Indice 1 · Je ne trouve pas Releases</summary>

Page d'accueil du dépôt, colonne de droite, sous « About ». S'il n'y a encore aucune release, le lien s'appelle **Create a new release**.
</details>

<details>
<summary>Indice 2 · Le correcteur ne voit pas ma release</summary>

Tu as peut-être cliqué sur **Save draft** : un brouillon n'est pas publié. Ouvre-le et clique sur **Publish release**. Vérifie aussi l'orthographe exacte du tag : `v0.1.0`.
</details>

<details>
<summary>Solution complète</summary>

Releases › Create a new release › Choose a tag › `v0.1.0` › Create new tag › titre › Generate release notes › Publish release › `/verifier`.
</details>

## Pièges fréquents

- Sauvegarder en brouillon au lieu de publier.
- Écrire `0.1.0` ou `V0.1.0` : la convention est un `v` minuscule.

## À retenir

Le versionnement sémantique se lit MAJEUR.MINEUR.CORRECTIF :

- `0.1.0` → `0.1.1` pour une correction de bug ;
- `0.1.0` → `0.2.0` pour une nouvelle fonctionnalité ;
- `1.0.0` quand l'appli est prête pour de vrais utilisateurs.
