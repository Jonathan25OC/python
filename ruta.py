import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    shortest_path_tree = {}
    last_connection = {}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                shortest_path_tree[neighbor] = current_node
                last_connection[neighbor] = (current_node, neighbor)

    return distances, shortest_path_tree, last_connection

def shortest_path(shortest_path_tree, start, target):
    path = []
    node = target
    while node != start:
        path.append(node)
        node = shortest_path_tree[node]
    path.append(start)
    path.reverse()
    return path

# Grafo del problema basado en la imagen proporcionada
graph = {
    'O': {'A': 2, 'B': 5, 'C': 4},
    'A': {'O': 2, 'B': 2, 'D': 7},
    'B': {'O': 5, 'A': 2, 'C': 1, 'D': 4, 'E': 3},
    'C': {'O': 4, 'B': 1, 'E': 4},
    'D': {'A': 7, 'B': 4, 'T': 5},
    'E': {'B': 3, 'C': 4, 'T': 7},
    'T': {'D': 5, 'E': 7}
}

start_node = 'O'
target_node = 'T'
distances, shortest_path_tree, last_connection = dijkstra(graph, start_node)
path = shortest_path(shortest_path_tree, start_node, target_node)

print(f"Distancias desde el nodo {start_node}: {distances}")
print(f"Árbol de caminos más cortos: {shortest_path_tree}")
print(f"Últimas conexiones: {last_connection}")
print(f"Ruta más corta desde {start_node} hasta {target_node}: {path}")
print(f"Distancia total de la ruta más corta: {distances[target_node]}")

# Creación del grafo usando NetworkX
G = nx.Graph()
for node in graph:
    for neighbor, weight in graph[node].items():
        G.add_edge(node, neighbor, weight=weight)

# Posiciones manuales de los nodos para que 'O' esté a la izquierda
pos = {
    'O': (0, 0),
    'A': (1, 2),
    'B': (2, 0),
    'C': (1, -2),
    'D': (4, 2),
    'E': (4, -2),
    'T': (5, 0)
}

# Dibuja todos los nodos y aristas
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f'{d["weight"]}' for u, v, d in G.edges(data=True)})

# Resalta el camino más corto
path_edges = list(zip(path, path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

plt.title(f'Ruta más corta de {start_node} a {target_node}: {" -> ".join(path)}\nDistancia total: {distances[target_node]}')
plt.show()