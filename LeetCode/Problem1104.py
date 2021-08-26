from typing import List
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        level = 0
        level_found = False
        while not level_found:
            level +=1
            if 2**(level-1) <= label <= (2**level) - 1:
                level_found = True
        result = [0]*level
        while level != 0:
            result[level-1] = label
            label = int(((2**level) - 1 - label + 2**(level-1))/2)
            level -= 1
        return result

ob = Solution()
print(ob.pathInZigZagTree(14))
print(ob.pathInZigZagTree(26))
print(ob.pathInZigZagTree(19))
print(ob.pathInZigZagTree(31))
print(ob.pathInZigZagTree(100))