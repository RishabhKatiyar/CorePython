from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        coloumns = len(grid[0])
        perimeter = 0
        for i in range(rows):
            for j in range(coloumns):
                if grid[i][j] == 1:
                    perimeter += 4
                    if j != 0:
                        perimeter -= grid[i][j-1]
                    if i != 0:
                        perimeter -= grid[i-1][j]
                    if j != len(grid[0])-1:
                        perimeter -= grid[i][j+1]
                    if i != len(grid)-1:
                        perimeter -= grid[i+1][j]

        return perimeter

ob = Solution()

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
#print(grid)
print(ob.islandPerimeter(grid))
#print(ob.grid)

grid = [[0,0,0,1],[1,1,1,1],[0,0,0,0],[0,0,0,1]]
#print(grid)
print(ob.islandPerimeter(grid))
#print(ob.grid)

grid = [[1,1],[1,1]]
print(ob.islandPerimeter(grid))