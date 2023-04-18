import random
import math

# Definir una función para calcular el valor y el peso de una mochila
def knapsack_value_weight(items, indices):
    value = sum([items[i][0] for i in indices])
    weight = sum([items[i][1] for i in indices])
    return value, weight

# Implementación de Recocido Simulado para resolver el problema de la mochila
def simulated_annealing_knapsack(items, max_weight):
    # Configuración de parámetros
    initial_temperature = 100
    cooling_rate = 0.03
    current_temperature = initial_temperature
    current_indices = list(range(len(items)))
    best_indices = current_indices
    best_value, best_weight = knapsack_value_weight(items, current_indices)

    # Bucle principal de Recocido Simulado
    while current_temperature > 1:
        # Generar una nueva solución aleatoria
        new_indices = current_indices.copy()
        i = random.randint(0, len(items) - 1)
        new_indices.remove(i)
        if knapsack_value_weight(items, new_indices)[1] <= max_weight:
            new_indices.append(i)

        # Calcular la diferencia de valor entre la nueva solución y la actual
        current_value, current_weight = knapsack_value_weight(items, current_indices)
        new_value, new_weight = knapsack_value_weight(items, new_indices)
        delta_value = new_value - current_value

        # Si la nueva solución es mejor, actualizar la mejor solución
        if delta_value > 0 and new_weight <= max_weight:
            current_indices = new_indices
            best_indices = new_indices
            best_value, best_weight = knapsack_value_weight(items, new_indices)
        # Si la nueva solución es peor, hay una probabilidad de aceptarla
        else:
            probability = math.exp(delta_value / current_temperature)
            if random.random() < probability and new_weight <= max_weight:
                current_indices = new_indices

        # Enfriar la temperatura
        current_temperature *= 1 - cooling_rate

    return best_indices, best_value

# Ejemplo de uso
items = [(0, 2), (3, 5), (2, 3), (1, 5), (1, 1),(3,3),(10,30),(10,30),(10,30),(10,30),(10,30),(10,30),(10,30),(10,30),(10,30),(10,30),(10,30),(10,30),(10,30),(10,30),(10,30),(10,30),(10,30)]
max_weight = 10

best_indices, best_value = simulated_annealing_knapsack(items, max_weight)
print("Mejores índices de elementos:", best_indices)
print("Mejor valor de la mochila:", best_value)