from typing import List
from sys import maxsize

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        repeating_indexes = []
        length = len(s)
        ch = s[0]
        prev = 0
        for i in range(1, length):
            if ch != s[i]:
                if i-1 - prev != 0:
                    repeating_indexes.append([prev, i-1])
                prev = i
                ch = s[i]
        if prev != length-1:
            repeating_indexes.append([prev, length-1])
        #print(repeating_indexes)

        total_cost = 0
        for repeating_index in repeating_indexes:
            start = repeating_index[0]
            end = repeating_index[1]
            max = -maxsize
            for i in range(start, end+1):
                total_cost += cost[i]
                if cost[i] > max:
                    max = cost[i]
            total_cost -= max
        return total_cost


ob = Solution()

s = "aabaa"
cost = [1,2,3,4,1]
print(ob.minCost(s, cost))

s = "abc"
cost = [1,2,3]
print(ob.minCost(s, cost))

s = "abaac"
cost = [1,2,3,4,5]
print(ob.minCost(s, cost))