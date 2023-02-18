import random
import sys
from matplotlib import pyplot as plt
import networkx as nx
from heapq import heappop, heappush
 

# Una clase para almacenar un nodo de heap
class Node:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight
 
    # Anule la función __lt__() para hacer que la clase `Node` funcione con un min-heap
    def __lt__(self, other):
        return self.weight < other.weight
 
 
# Una clase para representar un objeto graph
class Graph:
    def __init__(self, edges, n):
        # asigna memoria para la lista de adyacencia
        self.adjList = [[] for _ in range(n)]
 
        # agrega bordes al graph dirigido
        for (source, dest, weight) in edges:
            self.adjList[source].append((dest, weight))
 
 
def get_route(prev, i, route):
    if i >= 0:
        get_route(prev, prev[i], route)
        route.append(i)
 
 
# Ejecutar el algoritmo de Dijkstra en un graph dado
def findShortestPaths(graph, source, n):
 
    # crea un min-heap y empuja el nodo de origen con una distancia de 0
    pq = []
    heappush(pq, Node(source))
 
    # establece la distancia inicial desde la fuente a `v` como infinito
    dist = [sys.maxsize] * n
 
    # distancia de la fuente a sí mismo es cero
    dist[source] = 0
 
    # Lista # para rastrear vértices para los cuales ya se encontró el costo mínimo
    done = [False] * n
    done[source] = True
 
    # almacena el predecesor de un vértice (en una ruta de impresión)
    prev = [-1] * n
 
    # se ejecuta hasta que el min-heap esté vacío
    while pq:
 
        node = heappop(pq)      # Quitar y devolver el mejor vértice
        u = node.vertex         # obtener el número de vértice
 
        # hacer para cada vecino `v` de `u`
        for (v, weight) in graph.adjList[u]:
            if not done[v] and (dist[u] + weight) < dist[v]:        # Escalón de relajación
                dist[v] = dist[u] + weight
                prev[v] = u
                heappush(pq, Node(v, dist[v]))
 
        # marca el vértice `u` como hecho para que no se vuelva a recoger
        done[u] = True
 
    route = []
    for i in range(n):
        if i != source and dist[i] != sys.maxsize:
            get_route(prev, i, route)
            print(f'Camino de ({source} a {i}): Costo = {dist[i]}, Ruta = {route}')
            route.clear()
 
 
if __name__ == '__main__':
 
    # inicializa los bordes según el diagrama anterior
    # (u, v, w) representa la arista del vértice `u` al vértice `v` con peso `w`
   
    edges = [(0,1, 1), (0,2, 2), (0, 3, 3), (1,0, 1), (1, 2, 4), (2,0, 2), (2,1, 4), (2,3, 5),(3,0, 3),(3, 2, 5)]
    
    # número total de nodos en el graph (etiquetados de 0 a 3)
    n = 4
    
    # graph de construcción
    graph = Graph(edges, n)
   
    # ejecuta el algoritmo de Dijkstra desde cada nodo
    for source in range(n):
        findShortestPaths(graph, source, n)
        
    gra = nx.DiGraph()
    nx.draw(gra, with_labels=True)
    for node, neighbors,weight in edges:
         gra.add_edge(node, neighbors, weight=weight)
    
    pos = nx.spring_layout(gra)
    nx.draw(gra, pos, with_labels=True)
    edge_labels = nx.get_edge_attributes(gra, 'weight')
    nx.draw_networkx_edge_labels(gra, pos, edge_labels=edge_labels, font_size=8)
    plt.title(f'Grafo de tamaño {n}')
    plt.show()
   