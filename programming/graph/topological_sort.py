from collections import defaultdict, deque


def topologicalSort(jobs, deps):
    sorted_order = []
    graph = Graph(jobs, deps)
    print("Jobs ", jobs)
    print("Deps ", deps)
    print("Graph ", dict(graph.graph))
    print("In Degree ", graph.in_degree)

    queue = deque()
    for node, count in graph.in_degree.items():
        if count == 0:
            queue.append(node)
    print(queue)

    while len(queue) > 0:
        node = queue.popleft()
        sorted_order.append(node)
        for child in graph.graph[node]:
            graph.in_degree[child] -= 1
            if graph.in_degree[child] == 0:
                queue.append(child)

    if len(sorted_order) != len(jobs):
        return []
    return sorted_order


class Graph:
    def __init__(self, jobs, deps):
        self.graph = defaultdict(list)
        self.in_degree = {job: 0 for job in jobs}
        self.build_graph(jobs, deps)

    def build_graph(self, jobs, deps):
        for dep in deps:
            self.graph[dep[0]].append(dep[1])
            self.in_degree[dep[1]] += 1
