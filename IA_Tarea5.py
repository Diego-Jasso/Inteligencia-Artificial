import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    frontier = []
    heapq.heappush(frontier, (0, start))
    explored = set()
    parents = {start: None}

    while frontier:
        _, current_node = heapq.heappop(frontier)
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parents[current_node]
            return path[::-1]
        
        explored.add(current_node)
        for neighbor, weight in graph[current_node].items():
            if neighbor not in explored:
                priority = heuristic(neighbor, goal)
                heapq.heappush(frontier, (priority, neighbor))
                parents[neighbor] = current_node
                
    return None

# Ejemplo de uso
graph = {
    'A': {'B': 1, 'C': 5, 'D': 1},
    'B': {'A': 1, 'C': 4},
    'C': {'A': 5, 'B': 4, 'D': 1},
    'D': {'A': 1, 'C': 1}
}

heuristic = lambda n, goal: abs(ord(n) - ord(goal))

path = greedy_best_first_search(graph, 'B', 'D', heuristic)
if path:
    print('El camino más corto es:', path)
else:
    print('No se encontró un camino desde el nodo de inicio al nodo objetivo.')