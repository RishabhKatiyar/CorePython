from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        my_dict = {}
        for item in edges:
            first = item[0]
            second = item[1]
            if first in my_dict:
                my_dict[first][1].append(second)
                
            else:
                my_dict[first] = [False, [second]]
                
        #print(my_dict)

        for key in my_dict:
            for node in my_dict[key][1]:
                if node in my_dict and my_dict[node][0] == False:
                    my_dict[node][0] = True

        #print(my_dict)
        result = []
        for key in my_dict:
            if my_dict[key][0] == False:
                result.append(key)

        return result
        
        
ob = Solution()

n = 6
edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
print(ob.findSmallestSetOfVertices(n, edges))

n = 5
edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
print(ob.findSmallestSetOfVertices(n, edges))

n = 4
edges = [[2,0],[0,3],[3,1]]
print(ob.findSmallestSetOfVertices(n, edges))
