from typing import List
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows = len(box)
        coloumns = len(box[0])
        result_box = [[None]*rows for _ in range(coloumns)]
        result_coloumn = 0
        for row in range(rows - 1, -1, -1):
            last_pointer = coloumns - 1
            number_of_stones = 0
            for coloumn in range(coloumns - 1, -1, -1):
                if box[row][coloumn] == '#':
                    number_of_stones += 1
                if box[row][coloumn] == '*' or coloumn == 0:
                    if box[row][coloumn] == '*':
                        result_box[coloumn][result_coloumn] = '*'
                    current_pointer = coloumn + 1
                    if coloumn == 0:
                        current_pointer -= 1
                    if current_pointer <= coloumns - 1:
                        while last_pointer >= current_pointer:
                            if number_of_stones > 0:
                                result_box[last_pointer][result_coloumn] = '#'
                                number_of_stones -= 1
                            elif result_box[last_pointer][result_coloumn] != '*':
                                result_box[last_pointer][result_coloumn] = '.'
                            last_pointer -= 1
                    last_pointer = coloumn - 1
                if box[row][coloumn] == '.':
                    pass
            result_coloumn += 1
        return result_box

ob = Solution()
'''
box = [["#",".","*","."], ["#","#","*","."]]
print()
print(ob.rotateTheBox(box))
#box = [["#","#","#",".",".","*","#",".","#",".","*"]]
#print(ob.rotateTheBox(box))
print()
box = [["#",".","#"]]
print(ob.rotateTheBox(box))
print()
box = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
print(ob.rotateTheBox(box))
print()
'''

box = [["*"]]
print(ob.rotateTheBox(box))
print()