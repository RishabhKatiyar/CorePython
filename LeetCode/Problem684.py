from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        my_sets = [{i} for i in range(n)]
        my_dict = [i for i in range(n)]
        
        #print(my_sets)  
        #print(my_dict)   

        for edge in edges:
            left = edge[0]
            right = edge[1]

            index_left = my_dict[left - 1]
            index_right = my_dict[right - 1]

            if index_left == index_right:
                return edge

            my_sets[index_left] = my_sets[index_left].union(my_sets[index_right])

            if index_left != index_right:
                for item in my_sets[index_left]:
                    my_dict[item] = index_left        
                    my_sets[index_right] = set()

            #print(my_sets)  
            #print(my_dict)   

ob = Solution()


edges = [[1,2],[1,3],[2,3]]
print(ob.findRedundantConnection(edges))


edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print(ob.findRedundantConnection(edges))


edges = [[3,4],[1,2],[2,4],[3,5],[2,5]]
print(ob.findRedundantConnection(edges))
