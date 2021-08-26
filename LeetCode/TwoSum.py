class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        length = len(nums)
        map = {}
        for i in range(length):
            if target - nums[i] in map:
                a = i 
                b = map[target - nums[i]]
                if a>b:
                    return [b, a]
                else:
                   return [a, b]
            else:
                map[nums[i]] = i
        return [-1, -1]

nums = [2,7,11,15]
target = 9
ob = Solution()
print(ob.twoSum(nums, target))