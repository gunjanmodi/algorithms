def dijkstrasAlgorithm(start, edges):
    number_of_vertices = len(edges)

    min_distances = [float('inf') for _ in range(number_of_vertices)]
    min_distances[start] = 0

    visited = set()

    while len(visited) != number_of_vertices:
        vertex, current_min_distance = get_vertex_with_min_distance(min_distances, visited)

        if current_min_distance == float("inf"):
            break

        visited.add(vertex)

        for edge in edges[vertex]:
            destination, distance_to_destination = edge

            if destination in visited:
                continue

            new_path_distance = current_min_distance + distance_to_destination
            current_destination_distance = min_distances[destination]
            if new_path_distance < current_destination_distance:
                min_distances[destination] = new_path_distance
    return list(map(lambda x: -1 if x == float("inf") else x, min_distances))


def get_vertex_with_min_distance(distances, visited):
    current_min_distance = float("inf")
    vertex = -1

    for vertex_id, distance in enumerate(distances):
        if vertex_id in visited:
            continue
        if distance <= current_min_distance:
            vertex = vertex_id
            current_min_distance = distance

    return vertex, current_min_distance


if __name__ == '__main__':
    start = 0
    edges = [
        [
            [1, 7]
        ],
        [
            [2, 6],
            [3, 20],
            [4, 3]
        ],
        [
            [3, 14]
        ],
        [
            [4, 2]
        ],
        [],
        []
    ]
    dijkstrasAlgorithm(start, edges)
