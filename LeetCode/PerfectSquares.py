from sys import maxsize
from collections import deque

class Solution:
    def binarySearch(self, ps, n):
        low = 0
        high = len(ps)        
        
        while low <= high:
            mid = int((low + high)/2)
            if ps[mid] == n:
                break
            elif ps[mid] < n:
                low = mid + 1
            else:
                high = mid - 1
                
        if ps[mid] ==  n:
            return mid
        else:
            return low if low > high else high
            
    def numSquares(self, n: int) -> int:
        ps = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841,900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724, 6889, 7056, 7225, 7396, 7569, 7744, 7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801, 10000]
        index = self.binarySearch(ps, n)
        if ps[index] == n:
            return 1
        if ps[index] > n:
            index -= 1
        memo = set()
        queue = deque()
        for num in ps[:index+1]:
            queue.append([n, num, 0])

        min_so_far = maxsize
        count = 0
        while len(queue):
            count += 1
            res = queue.popleft()

            dividend = res[0]
            divisor = res[1]
            
            res[2] += int(dividend / divisor)
            res[0] = int(dividend % divisor)
            
            if min_so_far > res[2] and res[0] == 0 and res[2] <= 4:
                min_so_far =  res[2]
            else:
                index =  self.binarySearch(ps, res[0])
                if ps[index] > res[0]:
                    index -= 1
                for num in ps[:index+1]:
                    if not (res[0], num, res[2]) in memo:
                        memo.add((res[0], num, res[2]))
                        queue.append([res[0], num, res[2]])
        
        return min_so_far

ob = Solution()

print(ob.numSquares(10000))