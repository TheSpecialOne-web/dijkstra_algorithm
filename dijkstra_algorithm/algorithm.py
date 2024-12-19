import sys
import heapq

# Fonction pour calculer les distances minimales en carburant
def can_reach(start, N, fuel_max, graph, gas_stations):
    dist = [float('inf')] * N  # Distance de chaque ville initialisée à l'infini
    dist[start] = 0  # La distance de la ville de départ est 0
    pq = [(0, start)]  # File de priorité pour l'algorithme de Dijkstra
    
    while pq:
        fuel_used, node = heapq.heappop(pq)  # On prend la ville avec le moins de carburant utilisé
        
        # Si on est dans une station-service, on remet le carburant à 0
        if gas_stations[node] == 1:
            fuel_used = 0
        
        # On explore les voisins de la ville courante
        for neighbor, dist_to_neighbor in graph[node]:
            new_fuel_used = fuel_used + dist_to_neighbor
            
            # On ne considère que les trajets où le carburant utilisé ne dépasse pas la limite
            if new_fuel_used <= fuel_max and new_fuel_used < dist[neighbor]:
                dist[neighbor] = new_fuel_used
                heapq.heappush(pq, (new_fuel_used, neighbor))
    
    return dist

# Fonction principale qui résout le problème
def solve(N, M, L, gas_stations, roads):
    graph = [[] for _ in range(N)]  # Initialisation du graphe

    # Construction du graphe à partir des routes
    for u, v, d in roads:
        graph[u-1].append((v-1, d))  # Route bidirectionnelle entre u et v
        graph[v-1].append((u-1, d))
    
    # On obtient les distances minimales à partir de la ville 1 (index 0)
    reachable = can_reach(0, N, L, graph, gas_stations)
    
    # On compte combien de villes sont atteignables avec le carburant max L
    count = sum(1 for dist in reachable if dist <= L)
    
    # Si la ville de départ est atteignable, on la soustrait du comptage
    return count - 1 if reachable[0] <= L else count

# Fonction pour analyser les données d'entrée
def input_parser():
    input_data = sys.stdin.read().splitlines()  # Lire toutes les lignes d'entrée
    N, M, L = map(int, input_data[0].split())   # Extraire N, M, L
    gas_stations = [int(x) for x in input_data[1].strip()] # Extraire la liste des stations-service
    roads = []  # Liste pour les routes
    for line in input_data[2:]:  # Lire les routes
        u, v, d = map(int, line.split())  # Extraire les informations pour chaque route
        roads.append((u, v, d))  # Ajouter la route à la liste
    return N, M, L, gas_stations, roads

# Main - Entrée du programme
if __name__ == '__main__':
    N, M, L, gas_stations, roads = input_parser()  # Lire les données d'entrée
    print(solve(N, M, L, gas_stations, roads))  # Résoudre le problème et afficher la réponse
