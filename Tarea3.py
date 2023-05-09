import os 

with open('C:\\Users\\becar\\OneDrive\\Escritorio\\Sexto Semestre\\Inteligencia Artificial\\low-dimensional-instance.txt', 'r') as f:
    n, W = map(int, f.readline().split())
    values = []
    weights = []
    for i in range(n):
        line = f.readline().split()
        values.append(int(line[0]))
        weights.append(int(line[1]))

def heuristic(node):
    remaining_items = sorted(zip(values[node.level:], weights[node.level:]), key=lambda x: x[0]/x[1], reverse=True)
    total_value = node.value
    total_weight = node.weight
    for v, w in remaining_items:
        if total_weight + w <= W:
            total_value += v
            total_weight += w
        else:
            fraction = (W - total_weight) / w
            total_value += fraction * v
            break
    return total_value

class Node:
    def __init__(self, level, value, weight, selected_items):
        self.level = level
        self.value = value
        self.weight = weight
        self.selected_items = selected_items

def branch(node):
    if node.level >= n:
        return []
    left_node = Node(node.level + 1, node.value, node.weight, node.selected_items[:])
    right_node = Node(node.level + 1, node.value + values[node.level], node.weight + weights[node.level], node.selected_items[:] + [node.level])
    return [left_node, right_node]

def bound(node):
    if node.weight > W:
        return False
    if node.level == n:
        return True
    return heuristic(node) + node.value > best_value

root = Node(0, 0, 0, [])
queue = [root]
best_value = 0
best_items = []

while queue:
    node = queue.pop(0)
    if bound(node):
        if node.value > best_value:
            best_value = node.value
            best_items = node.selected_items
        queue.extend(branch(node))

selected_values = [values[i] for i in best_items]
selected_weights = [weights[i] for i in best_items]
print("Best value:", best_value)
print("Selected items:", best_items)
print("Selected values:", selected_values)
print("Selected weights:", selected_weights)