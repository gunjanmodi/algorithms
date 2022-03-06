class Solution:
    def countOrders(self, n: int) -> int:
        result = []
        
        def helper(pickup, deliveries, current):
            if len(current) == 2 * n:
                result.append(current[:])
                return
            
            for i in range(n):
                if not pickup[i]:
                    pickup[i] = True
                    current.append(f"P{i}")
                    helper(pickup, deliveries, current)
                    current.pop()
                    pickup[i] = False
                    
            for i in range(n):
                if pickup[i] and not deliveries[i]:
                    deliveries[i] = True
                    current.append(f"D{i}")
                    helper(pickup, deliveries, current)
                    current.pop()
                    deliveries[i] = False
        
        pickups = [False for _ in range(n)]
        deliveries = [False for _ in range(n)]
        helper(pickups, deliveries, [])
        return len(result)
        
            
if __name__ == '__main__':
    s = Solution()
    print(s.countOrders(1))
    print(s.countOrders(2))
    print(s.countOrders(3))
    print(s.countOrders(6))
    print(s.countOrders(8))