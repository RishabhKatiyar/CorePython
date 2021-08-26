class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = int((low + high) / 2)
            if target == nums[mid]:
                return mid
            if nums[low] <= target and target < nums[mid]:
                return self.binarySearch(nums, target, low, mid-1)
            
            elif nums[mid] < target and target <= nums[high]:
                return self.binarySearch(nums, target, mid+1, high)
            else:
                if target > nums[mid] and target > nums[low]:
                    low = mid - 1
                elif target > nums[mid]:
                    high = mid - 1
                elif target < nums[mid] and target < nums[high]: 
                    high = mid + 1
                elif target < nums[mid]:
                    low = mid + 1
                

    def binarySearch(self, nums, target, low, high):
        while low <= high:
            mid = int((low + high) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1


nums = [4,5,6,7,8,9,1,2,3]
ob = Solution()

print(ob.search(nums, 1))

'''
for num in nums:
    print(''.join(['#']*10))
    print(ob.search(nums, num))
    print(''.join(['#']*10))
    print()
'''