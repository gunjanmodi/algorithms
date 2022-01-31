class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}

        
    def make_set(self, n):
        for i in range(n):
            self.parent[i] = -1
            self.rank[i] = 0
    
    def find(self, x):
        if self.parent[x] == -1:
            return x
        return self.find(self.parent[x])
    
    def union(self, x, y):
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        elif self.rank[y] < self.rank[x]:
            self.parent[y] = x
        else:
            self.parent[y] = x
            self.rank[x] += 1


class Solution(object):
    def makeConnected(self, n, connections):

        ds = DisjointSet()
        ds.make_set(n)
        extra = 0
        for u, v in connections:
            x = ds.find(u)
            y = ds.find(v)
            
            if x != y:
                ds.union(x, y)
            else:
                extra += 1

        remaining_components = 0
        for i in range(n):
            if ds.parent[i] == -1:
                remaining_components += 1

        # the main disjoint will require a connection. Hence we are subtracting 1. 
        if extra >= remaining_components - 1:
            return remaining_components - 1
        else:
            return -1