import random
import heapq
import networkx as nx
import matplotlib.pyplot as plt

def generate_graph(n):
    graph = {}
    for i in range(n):
        neighbors = {}
        for j in range(n):
            if i != j:
                weight = random.randint(1, 10)
                neighbors[str(j)] = weight
        graph[str(i)] = neighbors
    return graph

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    previous_nodes = {node: None for node in graph}
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    return distances, previous_nodes

n = 3   # Tamaño del grafo
graph = generate_graph(n)


# Para cada nodo en el grafo, calcular las rutas más cortas a todos los demás nodos
for start_node in graph:
    distances, previous_nodes = dijkstra(graph, start_node)
    print(f'Rutas más cortas desde el nodo {start_node}:')
    for node in graph:
        if node == start_node:
            continue
        path = []
        current_node = node
        while current_node is not None:
            path.insert(0, current_node)
            current_node = previous_nodes[current_node]
        print(f'Ruta más corta a {node}: {path}')


# Crear grafo de networkx y agregar nodos y aristas
G = nx.DiGraph()
for node, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
        G.add_edge(node, neighbor, weight=weight)

# Dibujar grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
plt.title(f'Grafo de tamaño {n}')
plt.show()