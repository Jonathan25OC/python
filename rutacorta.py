import heapq

# Función para encontrar la ruta más corta usando el algoritmo de Dijkstra
def dijkstra(graph, start):
    # Diccionario que almacena la distancia mínima desde el nodo inicial
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0  # Distancia a sí mismo es 0
    priority_queue = [(0, start)]  # Inicializa la cola de prioridad con el nodo inicial
    shortest_path = {}  # Diccionario para almacenar el camino más corto

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Si la distancia actual es mayor que la mejor distancia registrada, continuamos
        if current_distance > distances[current_node]:
            continue

        # Revisa todos los nodos vecinos del nodo actual
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Si se encuentra una distancia menor, actualiza la distancia mínima
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, shortest_path

# Función para reconstruir el camino más corto desde el nodo inicial al objetivo
def shortest_route(shortest_path, start, target):
    path = []
    node = target

    while node != start:
        path.append(node)
        node = shortest_path[node]

    path.append(start)
    path.reverse()  # Invertir el camino para obtener el orden correcto
    return path

# Definimos el grafo (nodos y aristas con pesos)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Nodo inicial y nodo objetivo
start_node = 'A'
target_node = 'D'

# Llamar al algoritmo de Dijkstra
distances, shortest_path = dijkstra(graph, start_node)

# Mostrar los resultados
print(f"Distancia más corta desde {start_node} a todos los nodos: {distances}")
print(f"Ruta más corta desde {start_node} a {target_node}: {shortest_route(shortest_path, start_node, target_node)}")
