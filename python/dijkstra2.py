def dijkstra(graph, start):
    # Create dictionaries to store the shortest distance and parent nodes
    shortest_distance = {node: float('inf') for node in graph}
    shortest_distance[start] = 0
    parents = {node: None for node in graph}
    
    # Create a list to keep track of unvisited nodes
    unvisited_nodes = list(graph)
    
    while unvisited_nodes:
        # Find the node with the shortest known distance
        current_node = None
        for node in unvisited_nodes:
            if current_node is None or shortest_distance[node] < shortest_distance[current_node]:
                current_node = node
        
        # Remove the current node from the unvisited set
        unvisited_nodes.remove(current_node)
        
        # Calculate the tentative distance to each neighbor
        for neighbor, weight in graph[current_node].items():
            distance = shortest_distance[current_node] + weight
            
            # If this path is shorter than the previously recorded shortest distance, update it
            if distance < shortest_distance[neighbor]:
                shortest_distance[neighbor] = distance
                parents[neighbor] = current_node
    
    return shortest_distance, parents

# Example graph represented as an adjacency dictionary
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_distances, parents = dijkstra(graph, start_node)

# Function to construct the path from the parents dictionary
def construct_path(parents, start, end):
    path = []
    while end is not None:
        path.insert(0, end)
        end = parents[end]
    return path

print(shortest_distances)

# Print the shortest distances and paths
for node, distance in shortest_distances.items():
    path = construct_path(parents, start_node, node)
    print(f'Shortest distance from {start_node} to {node}: {distance}')
    print(f'Shortest path: {" -> ".join(path)}')
