from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.dic = {i:set() for i in range(n)}
                
        for connection in connections:
            source = connection[0]
            destination = connection[1]
            
            self.dic[source].add(destination)
            
        self.visited = set()
        self.canReachZero = set()
        count = 0

        for key in range(n):
            for destination in self.dic[key]:
                if not self.reachToZero(destination):
                    count += 1
                    self.dic[destination].add(0)

        return count
        
    def reachToZero(self, source):
        if source in self.canReachZero:
            return True
        result = False
        if source == 0:
            return True
        else:
            for destination in self.dic[source]:
                result |= self.reachToZero(destination)
                if result:
                    self.canReachZero.add(destination)
                    break
            if result:
                self.canReachZero.add(source)
            return result




ob = Solution()

n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
print(ob.minReorder(n, connections))


n = 5
connections = [[1,0],[1,2],[3,2],[3,4]]
print(ob.minReorder(n, connections))

n = 3
connections = [[1,0],[2,0]]
print(ob.minReorder(n, connections))


n = 6
connections = [[0,2],[0,3],[4,1],[4,5],[5,0]]
print(ob.minReorder(n, connections))
