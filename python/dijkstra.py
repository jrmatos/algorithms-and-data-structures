from collections import deque

def get_initial_costs_and_parents(graph, initial_node):
    visited = []
    costs = {}
    parents = {}

    for node in graph.keys():
        if node == initial_node:
            for start_neighboor in graph[node].keys():
                visited.append(start_neighboor)
                costs[start_neighboor] = graph[node][start_neighboor]
                parents[start_neighboor] = initial_node
        elif node not in visited:
            costs[node] = float('inf')
            parents[node] = None

    return costs, parents
                    

def get_example_1():
    graph = {}
    # start vertex
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2
    # a vertex
    graph["a"] = {}
    graph["a"]["end"] = 1
    # b vertex
    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["end"] = 5
    # end vertex
    graph["end"] = {}
    # parents
    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["end"] = None

    return graph, "start", "end"

def get_example_2():
    graph = {}
    graph["START"] = {}
    graph["START"]["A"] = 5
    graph["START"]["B"] = 2
    graph["A"] = {}
    graph["A"]["C"] = 4
    graph["A"]["D"] = 6
    graph["B"] = {}
    graph["B"]["A"] = 8
    graph["B"]["D"] = 7
    graph["C"] = {}
    graph["C"]["END"] = 3
    graph["C"]["D"] = 6
    graph["D"] = {}
    graph["D"]["END"] = 1
    graph["END"] = {}

    return graph, "START", "END"

def find_node_name_with_smallest_cost(costs, verified):
    # print("from costs", costs, "and verified", verified)
    cheapest_value = float('inf')
    cheapest_node = None

    for node_name in costs:
        cost = costs[node_name]

        if cost < cheapest_value and node_name not in verified:
            cheapest_value = cost
            cheapest_node = node_name

    # print("RELAXING ->", cheapest_node,
    #       " (because it is the cheapest one and not verified)")

    return cheapest_node

def get_path_from_parents_table(parents, start_node, end_node):
    current_node = end_node
    path = deque()

    while current_node in parents:
        path.appendleft(current_node)
        current_node = parents[current_node]

    path.appendleft(start_node)

    return tuple(path)

def dijkstra(graph, start_node, end_node):
    verified = []
    costs, parents = get_initial_costs_and_parents(graph, start_node)
    node_name = find_node_name_with_smallest_cost(costs, verified)

    while node_name != None and node_name != end_node:
        cost = costs[node_name]
        neighboors = graph[node_name]

        # print("current cost of", node_name, "is", cost)

        # print("start loop of neighboors", neighboors.keys())
        for neighboor in neighboors.keys():
            # print("|")
            # print("current neighboor", neighboor)
            # print("neighboor cost", neighboors[neighboor])
            new_cost = cost + neighboors[neighboor]
            # print("new cost to go to", neighboor, "is", new_cost)
            # print('if the new cost of ', new_cost,
            #       "is less than current cost of ", neighboor," (", costs[neighboor], ") ")
            if new_cost < costs[neighboor]:
                # print("-- then update cost of ", neighboor, " to ", new_cost)
                costs[neighboor] = new_cost
                parents[neighboor] = node_name
        #         print("-- also, parent of", neighboor, "is now", node_name)

        # print("end loop")

        # print("updated costs", costs)
        # print("updated parents", parents)
        # print("marking ", node_name, " as verified")
        verified.append(node_name)

        # print('\n')
        node_name = find_node_name_with_smallest_cost(costs, verified)

   
    return get_path_from_parents_table(parents, start_node, end_node), costs[end_node]

if __name__ == "__main__":
    graph, start_node, end_node = get_example_1()
    shortest_path, total_cost = dijkstra(graph, start_node, end_node)

    print("path", shortest_path)
    print("cost", total_cost)