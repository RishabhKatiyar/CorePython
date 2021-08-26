from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.result = []
        self.graph = graph
        self.destination = len(graph) - 1
        self.func(graph[0], [0])
        return self.result
        
    def func(self, edge, local_result):
        _local_result = local_result[:]
        #if len(edge) == 0 and _local_result[-1] == self.destination:
        #    self.result.append(_local_result)
        for node in edge:
            _local_result.append(node)
            if node == self.destination:
                self.result.append(_local_result[:])
            else:
                self.func(self.graph[node], _local_result)
            _local_result.pop(len(_local_result) - 1)

ob = Solution()            

graph = [[1,2],[3],[3],[]]
print(ob.allPathsSourceTarget(graph))

graph = [[4,3,1],[3,2,4],[3],[4],[]]
print(ob.allPathsSourceTarget(graph))

graph = [[1],[]]
print(ob.allPathsSourceTarget(graph))

graph = [[1,2,3],[2],[3],[]]
print(ob.allPathsSourceTarget(graph))


graph = [[1,3],[2],[3],[]]
print(ob.allPathsSourceTarget(graph))


graph = [[4,3,1],[3,2,4],[],[4],[]]
print(ob.allPathsSourceTarget(graph))


graph = [[2],[],[1]]
print(ob.allPathsSourceTarget(graph))