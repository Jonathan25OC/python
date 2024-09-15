import matplotlib.pyplot as plt
import networkx as nx

# Definir las actividades y sus tiempos (TO, TM, TP)
actividades = {
    'D': {'desc': 'Revisión del plano y planificación de la red', 'TO': 2, 'TM': 3, 'TP': 5},
    'E': {'desc': 'Instalación de puntos de acceso y conmutadores', 'TO': 3, 'TM': 5, 'TP': 8},
    'A': {'desc': 'Instalación de cableado', 'TO': 4, 'TM': 6, 'TP': 10},
    'B': {'desc': 'Configuración del servidor o router', 'TO': 2, 'TM': 4, 'TP': 8},
    'C': {'desc': 'Conexión y prueba de dispositivos', 'TO': 3, 'TM': 5, 'TP': 9},
    'F': {'desc': 'Configuración de seguridad de la red', 'TO': 2, 'TM': 3, 'TP': 6},
    'G': {'desc': 'Prueba y solución de problemas de la red', 'TO': 3, 'TM': 4, 'TP': 7},
}

# Calcular el tiempo esperado TE para cada actividad
for act, tiempos in actividades.items():
    TO = tiempos['TO']
    TM = tiempos['TM']
    TP = tiempos['TP']
    tiempos['TE'] = (TO + 4 * TM + TP) / 6

# Crear un gráfico de red (PERT) usando NetworkX
G = nx.DiGraph()

# Agregar nodos y aristas
for act, tiempos in actividades.items():
    G.add_node(act, label=f"{act}\n{tiempos['TE']:.2f} hrs")

# Definir las dependencias (secuencia de actividades)
dependencias = [('D', 'E'), ('E', 'A'), ('A', 'B'), ('B', 'C'), ('C', 'F'), ('F', 'G')]

G.add_edges_from(dependencias)

# Dibujar el diagrama de PERT
pos = nx.planar_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10)
labels = nx.get_node_attributes(G, 'label')
nx.draw_networkx_labels(G, pos, labels=labels)

plt.title("Diagrama PERT - Proyecto de Instalación de Internet")
plt.show()
