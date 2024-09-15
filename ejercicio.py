import matplotlib.pyplot as plt
import networkx as nx

# Crear un grafo dirigido
G = nx.DiGraph()

# Añadir nodos
nodes = ["O", "A", "B", "C", "D", "E", "F", "G"]
G.add_nodes_from(nodes)

# Añadir aristas con los tiempos esperados (te)
edges = [("O", "A", 1.58), ("O", "C", 2.67), ("A", "B", 2.00), ("C", "F", 1.58),
         ("B", "D", 2.00), ("B", "E", 3.67), ("B", "F", 2.00), ("D", "G", 1.00),
         ("E", "G", 1.00), ("F", "G", 1.00)]
G.add_weighted_edges_from(edges)

# Definir posiciones manualmente
pos = {
    "O": (-1.5, 0),
    "A": (-0.5, 1),
    "B": (0.5, 1),
    "C": (-0.5, -1),
    "D": (1.5, 1),
    "E": (1, 0),
    "F": (0.5, -1),
    "G": (1.5, 0)
}

# Definir la ruta específica para resaltar: O -> A -> B -> D -> G
highlighted_path = ["O", "A", "B", "D", "G"]
highlighted_path_edges = list(zip(highlighted_path, highlighted_path[1:]))

# Dibujar el grafo
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=16, font_weight='bold', arrowsize=20)
nx.draw_networkx_edges(G, pos, edgelist=highlighted_path_edges, edge_color='red', width=2)

# Añadir etiquetas de los pesos
edge_labels = {(u, v): f'{d["weight"]:.2f}' for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

# Mostrar la gráfica
plt.title('Ruta O -> A -> B -> D -> G en rojo')
plt.show()