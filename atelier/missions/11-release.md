titre: Mission 11 · Publier une version
labels: mission, palier-4
---
## Pourquoi

Une release fige un état stable de ton appli, avec un nom (`v0.1.0`) et des notes. Si une future PR de l'IA casse tout, tu sais exactement vers quelle version revenir, et ce qu'elle contenait.

## Étapes

1. Sur la page d'accueil du dépôt, colonne de droite : **Releases** › **Create a new release**.
2. **Choose a tag** › tape `v0.1.0` › **Create new tag: v0.1.0 on publish**. Cible : `main`.
3. Titre : `v0.1.0 · Première version stable`.
4. Clique sur **Generate release notes** : GitHub liste automatiquement les PR fusionnées. Relis-les : c'est le journal de ton projet.
5. **Publish release**.

## Valider

Commente `/verifier` sur cette issue.

## À retenir

Le versionnement sémantique se lit MAJEUR.MINEUR.CORRECTIF :

- `0.1.0` → `0.1.1` pour une correction de bug ;
- `0.1.0` → `0.2.0` pour une nouvelle fonctionnalité ;
- `1.0.0` quand l'appli est prête pour de vrais utilisateurs.
