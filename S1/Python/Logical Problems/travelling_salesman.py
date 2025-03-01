def calculate_distance(path, distance_matrix):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distance_matrix[path[i]][path[i + 1]]
    total_distance += distance_matrix[path[-1]][path[0]]
    return total_distance

def find_shortest_path(distance_matrix):
    n = len(distance_matrix)
    cities = list(range(n))
    min_distance = float('inf')
    best_path = []

    def generate_paths(path, remaining):
        nonlocal min_distance, best_path
        if not remaining:
            path_distance = calculate_distance(path, distance_matrix)
            if path_distance < min_distance:
                min_distance = path_distance
                best_path = path[:]
            return

        for i in range(len(remaining)):
            generate_paths(path + [remaining[i]], remaining[:i] + remaining[i+1:])

    generate_paths([0], cities[1:])  # Start with city 0
    return best_path, min_distance

distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

optimal_path, optimal_distance = find_shortest_path(distance_matrix)
print(f"Optimal Path: {optimal_path}")
print(f"Optimal Distance: {optimal_distance}")