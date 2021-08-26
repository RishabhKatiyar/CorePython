class Solution:
    def findMin(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1
        import sys
        min = sys.maxsize

        while low <= high:
            
            mid = int((low + high)/2)
            if nums[low] <= nums[mid]:
                min = nums[low] if nums[low] < min else min
                low = mid + 1
            elif nums[high] >= nums[mid]:
                min = nums[mid] if nums[mid] < min else min
                high = mid - 1
        return min

#nums = [0, 1, 2, 3, 4, 5]
#nums = [5, 0, 1, 2, 3, 4]
#nums = [4, 5, 0, 1, 2, 3]
#nums = [3, 4, 5, 0, 1, 2]
#nums = [2, 3, 4, 5, 0, 1]
#nums = [1, 2, 3, 4, 5, 0]
#nums = [0, 1, 2, 3, 4, 5]
#nums = [0, 1, 2, 3, 4, 5]
#nums = [0, 1, 2, 3, 4, 5]
#nums = [0, 1, 2, 3, 4, 5]
nums = [7,8,1,2,3,4,5,6]
#nums = [1]
#nums = [4,5,6,7,0,1,2]
ob = Solution()
print(ob.findMin(nums))