class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        return int(len(nums)*(len(nums)+1)/2 - sum(nums))

nums = [3,0,1]
ob = Solution()
print(ob.missingNumber(nums))