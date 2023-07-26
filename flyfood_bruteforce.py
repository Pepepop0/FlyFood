
def calculate_distance(point1, point2):
    return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])


def create_distance_matrix(points):
    matrix = []
    for i in range(len(points)):
        row = []
        for j in range(len(points)):
            row.append(calculate_distance(points[i], points[j]) if i != j else 0)
        matrix.append(row)
    return matrix

def permutations(route):
    if len(route) <= 1:
        return [route]
    else:
        perms = []
        for i in range(len(route)):
            rest = route[:i] + route[i+1:]
            for p in permutations(rest):
                perms.append(route[i:i+1] + p)
        return perms

def brute_force_tsp(points):
    num_locations = len(points)
    routes = permutations(list(range(num_locations)))
    distances_matrix = create_distance_matrix(points)
    best_route = None
    best_distance = float('inf')

    for route in routes:
        route_distance = sum(distances_matrix[route[i-1]][route[i]] for i in range(num_locations))
        if route_distance < best_distance:
            best_route = route
            best_distance = route_distance

    return best_route, best_distance

# Teste com 4 pontos de entrega
points_4 = [(1, 1), (1, 2), (2, 1), (2, 2)]
route, distance = brute_force_tsp(points_4)
print(f"4 pontos de entrega: rota = {route}, distância = {distance}")

# Teste com 6 pontos de entrega
points_6 = [(1, 1), (1, 2), (2, 1), (2, 2), (1, 3), (2, 3)]
route, distance = brute_force_tsp(points_6)
print(f"6 pontos de entrega: rota = {route}, distância = {distance}")

# Teste com 8 pontos de entrega
points_8 = [(1, 1), (1, 2), (2, 1), (2, 2), (1, 3), (2, 3), (3, 1), (3, 2)]
route, distance = brute_force_tsp(points_8)
print(f"8 pontos de entrega: rota = {route}, distância = {distance}")
