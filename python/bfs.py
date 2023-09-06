from collections import deque

def get_graph():
    graph = {}
    graph["you"] = ["alice", "bob", "cleire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["cleire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []

    return graph

def is_what_we_need(item):
    return item == "jonny"

def BFS(graph, name):
    search_queue = deque()
    search_queue += graph[name]
    verified = []

    while search_queue:
        person = search_queue.popleft()

        if not person in verified:
            if is_what_we_need(person):
                return True
            else:
                search_queue += graph[person]
                verified.append(person)

    return False

if __name__ == "__main__":
    graph = get_graph()
    print(BFS(graph, 'you'))
