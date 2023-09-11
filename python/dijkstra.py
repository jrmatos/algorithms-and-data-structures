def find_node_name_with_smallest_cost(costs, verified):
    print("from costs", costs, "and verified", verified)
    cheapest_value = float('inf')
    cheapest_node = None

    for node_name in costs:
        cost = costs[node_name]

        if cost < cheapest_value and node_name not in verified:
            cheapest_value = cost
            cheapest_node = node_name

    print("RELAXING ->", cheapest_node,
          " (because it is the cheapest one and not verified)")

    return cheapest_node


if __name__ == "__main__":
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
    # costs with initial values
    costs = {}
    costs["a"] = 6
    costs["b"] = 2
    costs["end"] = float('inf')
    # parents
    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["end"] = None
    print("parents", parents)

    verified = []
    node_name = find_node_name_with_smallest_cost(costs, verified)

    while node_name is not None:

        cost = costs[node_name]
        neighboors = graph[node_name]

        print("current cost", node_name, cost)

        print("start loop of neighboors", neighboors.keys())
        for n in neighboors.keys():
            print("|")
            print("current neighboor", n)
            print("neighboor cost", neighboors[n])
            new_cost = cost + neighboors[n]
            print("new cost to go to", n, "is", new_cost)
            print('if the current cost of ', n,
                  " (", costs[n], ") is greater than ", new_cost)
            if costs[n] > new_cost:
                print("-- then update cost of ", n, " to ", new_cost)
                costs[n] = new_cost
                parents[n] = node_name
                print("-- also, parent of", n, "is now", node_name)

        print("end loop")

        print("updated costs", costs)
        print("updated parents", parents)
        print("marking ", node_name, " as verified")
        verified.append(node_name)

        print('\n')
        node_name = find_node_name_with_smallest_cost(costs, verified)

    print("solution (parents table)", parents)
