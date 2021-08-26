class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        _set = set()
        for num in nums:
            if num in _set:
                return True
            else:
                _set.add(num)
        return False



nums = [1,2,3,4]
ob = Solution()
print(ob.containsDuplicate(nums))