def load_instance(file_path):
    with open(file_path, 'r') as f:
        n, W = map(float, f.readline().split())
        items = []
        for line in f:
            v, w = map(float, line.split())
            items.append((v, w))
    return n, W, items

from queue import Queue

def knapsack_bfs(file_path):
    # Cargar datos de la instancia
    n, W, items = load_instance(file_path)

    # Inicializar la cola de nodos pendientes
    queue = Queue()
    queue.put((0, 0, []))  # (valor, peso, objetos)

    # Inicializar la mejor solución encontrada
    best_value = 0
    best_items = []

    # Ejecutar el algoritmo de búsqueda en amplitud
    while not queue.empty():
        value, weight, chosen_items = queue.get()

        # Si no podemos agregar más objetos a la mochila, detener la expansión
        if weight >= W:
            continue

        # Expandir el nodo actual agregando el siguiente objeto
        for i in range(len(items)):
            if i not in chosen_items:
                v, w = items[i]
                new_value = value + v
                new_weight = weight + w
                new_chosen_items = chosen_items + [i]

                # Si la nueva combinación de objetos no excede la capacidad de la mochila y tiene un valor mayor
                # que la mejor solución encontrada hasta ahora, agregarla a la cola y actualizar la mejor solución
                if new_weight <= W and new_value > best_value:
                    best_value = new_value
                    best_items = new_chosen_items
                queue.put((new_value, new_weight, new_chosen_items))

    # Devolver la mejor solución encontrada
    return best_value, best_items

best_value, best_items = knapsack_bfs('5')
print('Valor máximo:', best_value)
print('Objetos elegidos:', best_items)