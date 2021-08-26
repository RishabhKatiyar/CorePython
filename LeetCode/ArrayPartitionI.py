from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        index = 1
        sum = 0
        length = len(nums)
        for index in range(0, length, 2):
            sum += nums[index]
        return sum


nums = [1,4,3,2]
ob = Solution()
print(ob.arrayPairSum(nums))