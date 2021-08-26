import math
class Solution:
    def findNthDigit(self, n: int) -> int:
        _str = ""
        len_of_string = 0
        last_good_index = 0
        for i in range(1, n+1):
            len_of_string += int(math.log10(i))+1
            if len_of_string >= n:                
                result = str(i)[n - last_good_index - 1]
                break
            else:
                last_good_index = len_of_string
        return int(result)

ob = Solution()
print(ob.findNthDigit(2**31 -1))