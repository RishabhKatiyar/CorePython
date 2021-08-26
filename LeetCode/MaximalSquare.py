from typing import List
class Solution:
    matrix = None
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        self.matrix = matrix
        max_so_far = 0
        rows = len(self.matrix)
        coloumns = len(self.matrix[0])
        area = 0

        for i in range(rows):
            for j in range(coloumns):
                #print(self.matrix[i][j], end = '\t')
                if self.matrix[i][j] == "1":
                    iteration = 0
                    area = 1

                    while self.checkRightAndBottomBoundaries(i, j, i + iteration, j + iteration):
                        iteration += 1
                        area += 1

                    if max_so_far < area:
                        max_so_far = area    
        
        #print(max_so_far * max_so_far)
        #self.checkRightAndBottomBoundaries((0,0), (0,0))
        return max_so_far * max_so_far
           

    def checkRightAndBottomBoundaries(self, start_i, start_j, end_i, end_j):
        #print(start_i, start_j, end_i, end_j)
        try:
            i = end_i + 1
            for j in range(start_j, end_j + 1):
                #print(self.matrix[i][j], end = '\t')
                if self.matrix[i][j] == "0":
                    return False
            #print()
            j = end_j + 1
            for i in range(start_i, end_i + 1 + 1):
                #print(self.matrix[i][j])
                if self.matrix[i][j] == "0":
                    return False
        except:
            return False
        return True


ob = Solution()

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(ob.maximalSquare(matrix))

matrix = [["0","1"],["1","0"]]
print(ob.maximalSquare(matrix))