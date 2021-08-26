class Solution:
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums) - 1
        mid = -1

        if target > nums[high]:
            return len(nums)
        if target < nums[0]:
            return 0

        while low <= high and nums[low] <= target and target <= nums[high]:
            mid = int((low + high)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return low

ob = Solution()

nums = [1,3,5,7,9,11,13,15,17]
target = 4
print(ob.searchInsert(nums, target))