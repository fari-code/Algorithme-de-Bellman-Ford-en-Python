def bellman_ford(n, edges, source):
    """
    Calcule les plus courtes distances depuis une source.

    Paramètres :
        n      : nombre de sommets, numérotés de 0 à n-1
        edges  : liste d'arêtes (u, v, poids)
        source : sommet de départ

    Retourne :
        (dist, pred, False) si aucun cycle négatif accessible
        (None, pred, True) si un cycle négatif accessible existe
    """
    if n <= 0:
        raise ValueError("Le nombre de sommets doit être positif.")

    if not 0 <= source < n:
        raise ValueError("Le sommet source est invalide.")

    for u, v, _ in edges:
        if not (0 <= u < n and 0 <= v < n):
            raise ValueError(f"Arête invalide : ({u}, {v}).")

    # Initialisation
    dist = [float("inf")] * n
    pred = [None] * n
    dist[source] = 0

    # Relaxation des arêtes au maximum n - 1 fois
    for _ in range(n - 1):
        updated = False

        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pred[v] = u
                updated = True

        # Optimisation : aucune distance n'a changé
        if not updated:
            break

    # Détection d'un cycle négatif accessible depuis la source
    for u, v, w in edges:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            return None, pred, True

    return dist, pred, False


def reconstruct_path(pred, source, target):
    """
    Reconstruit le chemin de source à target.
    Retourne None si target est inaccessible depuis source.
    """
    if not (0 <= source < len(pred) and 0 <= target < len(pred)):
        raise ValueError("La source ou la cible est invalide.")

    path = []
    current = target

    while current is not None:
        path.append(current)

        if current == source:
            path.reverse()
            return path

        current = pred[current]

    return None


def main():
    # Exemple : graphe de 5 sommets numérotés de 0 à 4
    edges = [
        (0, 1, 6),
        (0, 2, 7),
        (1, 2, 8),
        (1, 3, 5),
        (1, 4, -4),
        (2, 3, -3),
        (2, 4, 9),
        (3, 1, -2),
        (4, 0, 2),
        (4, 3, 7),
    ]

    n = 5
    source = 0

    distances, predecessors, cycle = bellman_ford(n, edges, source)

    if cycle:
        print("Cycle de poids négatif détecté !")
        return

    print(f"Distances depuis le sommet {source} :")
    for vertex, distance in enumerate(distances):
        valeur = distance if distance != float("inf") else "∞ (inaccessible)"
        print(f"  Vers {vertex} : {valeur}")

    print("\nChemins :")
    for target, distance in enumerate(distances):
        if distance == float("inf"):
            print(f"  Vers {target} : inaccessible")
            continue

        path = reconstruct_path(predecessors, source, target)
        if path is not None:
            chemin = " → ".join(map(str, path))
            print(f"  {source} → {target} : {chemin} (coût = {distance})")


if __name__ == "__main__":
    main()