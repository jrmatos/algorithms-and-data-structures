from collections import deque

def dijkstra(graph, start_node):
    # init shortest_distances, parents and unvisited
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start_node] = 0
    parents = {node: None for node in graph}
    unvisited = list(graph)

    while unvisited:
        current_node = None

        # find node with shortest known distance
        for node in unvisited:
            if current_node is None or shortest_distances[node] < shortest_distances[current_node]:
                current_node = node

        for neighboor, weight in graph[current_node].items():

            new_cost = shortest_distances[current_node] + weight

            if new_cost < shortest_distances[neighboor]:
                shortest_distances[neighboor] = new_cost
                parents[neighboor] = current_node

        unvisited.remove(current_node)

    return shortest_distances, parents

def construct_path(parents, end):
    path = deque()
    while end is not None:
        path.appendleft(end)
        end = parents[end]

    return path

# graph = {
#     'A': {'B': 1, 'C': 4},
#     'B': {'A': 1, 'C': 2, 'D': 5},
#     'C': {'A': 4, 'B': 2, 'D': 1},
#     'D': {'B': 5, 'C': 1}
# }

graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'D': 2, 'E': 4},
    'C': {'E': 1},
    'D': {'G': 6, 'H': 3},
    'E': {'I': 2},
    'F': {'J': 4},
    'G': {'I': 1},
    'H': {'I': 2},
    'I': {'J': 3},
    'J': {},
}

start_node = 'A'
shortest_distances, parents = dijkstra(graph, start_node)

print(shortest_distances)
print(parents)
print(construct_path(parents, 'J'))
