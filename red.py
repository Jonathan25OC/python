import networkx as nx
import matplotlib.pyplot as plt

def crear_topologia_estrella(num_nodos):
    # Crear un grafo vacío
    G = nx.Graph()
    
    # Asignar la dirección IP al nodo central (servidor principal)
    ip_centro = "192.168.0.1"
    G.add_node("Centro", ip=ip_centro)
    
    # Añadir nodos y conectarlos al nodo central
    for i in range(1, num_nodos + 1):
        nodo = f"Edificio_{i}"
        ip_nodo = f"192.168.0.{i + 1}"  # Asignar IP única a cada nodo
        G.add_node(nodo, ip=ip_nodo)
        G.add_edge("Centro", nodo)
    
    return G

def mostrar_topologia(G):
    # Dibujar la topología de estrella
    pos = nx.spring_layout(G)  # Layout de la red para una mejor visualización
    labels = {nodo: f"{nodo}\n{G.nodes[nodo]['ip']}" for nodo in G.nodes()}  # Etiquetas con IPs
    nx.draw(G, pos, labels=labels, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold', edge_color='gray')
    
    # Mostrar las conexiones
    plt.title("Topología en Estrella con IPs")
    plt.show()

# Número de edificios (nodos) que quieres conectar
num_edificios = 9


# Crear y mostrar la topología en estrella
G = crear_topologia_estrella(num_edificios)
mostrar_topologia(G)

