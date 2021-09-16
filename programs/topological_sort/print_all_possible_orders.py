from collections import deque

def print_orders(tasks, prerequisites):
    sorted_order = []
    if tasks <= 0:
        return False

    # Initialize the graph
    in_degree = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}

    # Build the graph
    for prerequisite in prerequisites:
        parent, child = prerequisite[0], prerequisite[1]
        graph[parent].append(child)
        in_degree[child] += 1

    # Initialize the queue
    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    print_all_topologic_sorts(graph, in_degree, sources, sorted_order)

def print_all_topologic_sorts(graph, in_degree, sources, sorted_order):
    if sources:
        for vertex in sources:
            sorted_order.append(vertex)
            sources_for_next_call = deque(sources)
            sources_for_next_call.remove(vertex)
            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources_for_next_call.append(child)
            print_all_topologic_sorts(graph, in_degree, sources_for_next_call, sorted_order)
        
        sorted_order.remove(vertex)
        for child in graph[vertex]:
            in_degree[child] += 1

    if len(sorted_order) == len(in_degree):
        print(sorted_order)


def main():
    print("Task Orders: ")
    print_orders(3, [[0, 1], [1, 2]])

    print("Task Orders: ")
    print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

    print("Task Orders: ")
    print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()