from collections import deque


def topological_sort(vertices, edges):

    sorted_order = []
    if vertices <= 0:
        return sorted_order

    # Initialize the graph where source will be the key and value will be the children of that node.
    graph = {i: [] for i in range(vertices)}
    # Make the dictionary with counts
    in_degree = {i: 0 for i in range(vertices)}

    # Append the value of the graph by traversing the list
    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)
        in_degree[child] += 1

    # Implement BFS: Create a dequeue
    queue = deque()
    for key in graph:
        if in_degree[key] == 0:
            queue.append(key)
    print(queue)
    # try reducing the source that mean whenever indegree will be zero then append in the queue

    while len(queue) > 0:
        vertex = queue.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                queue.append(child)

    return sorted_order


    

def main():
  print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
  print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
  print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()