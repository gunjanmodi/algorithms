from collections import defaultdict


def find(u, parent):
    if parent[u] == -1:
        return u
    if parent[u] != -1:
        return find(parent[u], parent)


def union(parent, rank, x, y):
    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[y] < rank[x]:
        parent[y] = x
    else:
        parent[y] = x
        rank[x] += 1
        

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = defaultdict(int)
        rank = defaultdict(int)
        
        for u, v in edges:
            parent[u] = -1
            parent[v] = -1
            rank[u] = 0
            rank[v] = 0

        i = 0
        vertices = len(parent.keys())

        while i < vertices:
            edge = edges[i]
            x = find(edge[0], parent)
            y = find(edge[1], parent)
            if x != y:
                union(parent, rank, x, y)  
            else:
                return edge
            i += 1    


if __name__ == '__main__':
    is_connected = [[1,2],[1,3],[2,3]]
    result = Solution().findRedundantConnection(is_connected)
    print(result)