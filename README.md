# Algorithme de Bellman-Ford en Python

Ce projet implémente l'algorithme de **Bellman-Ford** pour calculer les plus courtes distances depuis un sommet source vers les autres sommets d'un graphe orienté pondéré.

L'algorithme accepte les arêtes de poids négatif et détecte les cycles de poids négatif accessibles depuis le sommet source.

## Fonctionnalités

- Calcul des plus courtes distances depuis une source.
- Gestion des poids positifs, nuls et négatifs.
- Reconstruction d'un chemin à l'aide des prédécesseurs.
- Signalement des sommets inaccessibles.
- Détection des cycles de poids négatif accessibles depuis la source.
- Arrêt anticipé lorsqu'une itération ne modifie aucune distance.

## 1. Principe de l'algorithme

Bellman-Ford commence par attribuer la distance `0` au sommet source et l'infini aux autres sommets. Ensuite, il examine toutes les arêtes et met à jour les distances lorsqu'un chemin plus court est trouvé. Cette opération s'appelle la **relaxation**.

Pour un graphe contenant `V` sommets, toutes les arêtes sont relaxées au maximum `V - 1` fois. Un dernier passage permet de détecter un cycle de poids négatif accessible depuis la source.

### Pseudo-code

```text
ALGORITHME BellmanFord(n, aretes, source)

    POUR chaque sommet v de 0 à n - 1 FAIRE
        distance[v] <- INFINI
        pred[v] <- AUCUN
    FIN POUR

    distance[source] <- 0

    // Relaxation des arêtes
    POUR i de 1 à n - 1 FAIRE
        modifie <- FAUX

        POUR chaque arête (u, v, poids) dans aretes FAIRE
            SI distance[u] != INFINI ET
               distance[u] + poids < distance[v] ALORS

                distance[v] <- distance[u] + poids
                pred[v] <- u
                modifie <- VRAI
            FIN SI
        FIN POUR

        SI modifie = FAUX ALORS
            QUITTER LA BOUCLE
        FIN SI
    FIN POUR

    // Détection d'un cycle de poids négatif
    POUR chaque arête (u, v, poids) dans aretes FAIRE
        SI distance[u] != INFINI ET
           distance[u] + poids < distance[v] ALORS
            RETOURNER AUCUNE_DISTANCE, pred, VRAI
        FIN SI
    FIN POUR

    RETOURNER distance, pred, FAUX

FIN ALGORITHME
```

### Pseudo-code de reconstruction d'un chemin

```text
ALGORITHME ReconstruireChemin(pred, source, cible)

    chemin <- liste vide
    courant <- cible

    TANT QUE courant != AUCUN FAIRE
        Ajouter courant à chemin

        SI courant = source ALORS
            Inverser chemin
            RETOURNER chemin
        FIN SI

        courant <- pred[courant]
    FIN TANT QUE

    // La source n'a pas été retrouvée : cible inaccessible
    RETOURNER AUCUN

FIN ALGORITHME
```




## 4. Comment exécuter le programme ?

Python  est nécessaire. Depuis le terminal, placez-vous dans le dossier du projet puis lancez :

```bash
python main.py
```

Sous Windows, cette commande fonctionne également dans PowerShell. Selon l'installation de Python, il est aussi possible d'utiliser :

```powershell
py main.py
```

## 5. Comment tester les cas particuliers ?

### Test A — Cycle de poids négatif

Utilisez temporairement ce graphe :

```python
n = 3
source = 0
edges = [
    (0, 1, 1),
    (1, 2, -3),
    (2, 1, 1),
]
```

Le cycle `1 → 2 → 1` a un poids total de `-2`. Le programme doit signaler un cycle négatif accessible depuis la source.

### Test B — Sommet inaccessible

Utilisez temporairement ce graphe :

```python
n = 3
source = 0
edges = [
    (0, 1, 5),
]
```

Le sommet `2` est inaccessible depuis `0`. Sa distance doit rester infinie et le programme doit l'afficher comme inaccessible, sans reconstruire de chemin pour lui.

## 6. Comprendre les variables

| Variable | Rôle |
|---|---|
| `n` | Nombre de sommets du graphe |
| `edges` | Liste des arêtes `(départ, arrivée, poids)` |
| `source` | Sommet depuis lequel les distances sont calculées |
| `dist` | Distance minimale connue vers chaque sommet |
| `pred` | Prédécesseur de chaque sommet pour reconstruire un chemin |
| `updated` | Indique si une distance a été modifiée pendant une itération |
| `cycle` | Indique la détection d'un cycle de poids négatif accessible |

## 7. Complexité

- **Temps :** `O(V × E)`, où `V` est le nombre de sommets et `E` le nombre d'arêtes.
- **Mémoire supplémentaire :** `O(V)` pour les tableaux de distances et de prédécesseurs, hors stockage des arêtes.

## 8. Limites et remarques

- Les sommets sont numérotés de `0` à `n - 1`.
- Chaque arête `(u, v, poids)` représente une direction de `u` vers `v`. Pour représenter les deux directions, ajouter les deux arêtes.
- Les poids peuvent être positifs, nuls ou négatifs.
- Le programme détecte uniquement les cycles négatifs **accessibles depuis la source**.
- Si un cycle négatif accessible est détecté, les plus courtes distances ne sont pas définies pour les sommets affectés par ce cycle ; le programme signale donc la situation au lieu de présenter les distances comme définitives.

---

**Auteur :** 
**Langage :** Python
**Algorithme :** Bellman-Ford
