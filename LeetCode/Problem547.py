from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        number_of_nodes = len(isConnected[0])
        number_of_rows = len(isConnected)
        
        my_sets = [{i} for i in range(number_of_nodes)]
        my_dict = [i for i in range(number_of_nodes)]
        
        result = number_of_nodes
        
        for i in range(number_of_rows):
            for j in range(i+1, number_of_nodes):
                if isConnected[i][j] == 1:
                    index_i = my_dict[i]
                    index_j = my_dict[j]
                    my_sets[index_i] = my_sets[index_i].union(my_sets[index_j])
                    
                    if index_j != index_i:
                        for item in my_sets[index_i]:
                            my_dict[item] = index_i
                            
                        my_sets[index_j] = set()
                        result -= 1
                        
        return result


ob = Solution()

isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
print(ob.findCircleNum(isConnected))

isConnected = [[1,1,1],[1,1,1],[1,1,1]]
print(ob.findCircleNum(isConnected))

isConnected = [[1,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,1,1,0,0],[0,0,0,1,0,0,0,0,1,1],[0,0,0,0,1,0,0,1,0,0],[0,0,0,0,0,1,0,1,1,1],[0,0,1,0,0,0,1,0,0,1],[0,0,1,0,1,1,0,1,0,0],[0,0,0,1,0,1,0,0,1,0],[0,0,0,1,0,1,1,0,0,1]]
print(ob.findCircleNum(isConnected))

isConnected = [[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],[1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],[0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]]
print(ob.findCircleNum(isConnected))