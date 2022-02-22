class Solution(object):
    def findCircleNum(self, is_connected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        parent = [-1] * len(is_connected)
        edges = len(is_connected)
        i = 0
        while i < len(is_connected):
            j = 0
            while j <= i:
                if i != j and is_connected[i][j] == 1:
                    x = self.find(i, parent)
                    y = self.find(j, parent)

                    if x != y:
                        self.union(parent, x, y)
                        edges -= 1
                j += 1
            i += 1
        return edges
    
    def find(self, u, parent):
        if parent[u] == -1:
            return u
        if parent[u] != -1:
            return self.find(parent[u], parent)
        
    
    def union(self, parent, x, y):
        parent[x] = y


if __name__ == '__main__':
    is_connected = [[1,1,0],[1,1,0],[0,0,1]]
    result = Solution().findCircleNum(is_connected)
    print(result)