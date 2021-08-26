from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        index = self.binarySearch(nums, target, 0, len(nums) - 1)
        #print(f'Index = {index}')
        if index == -1:
            return [-1, -1]
        right_index = index
        left_index = index
        result = index
        while result != -1:
            result = self.binarySearch(nums, target, right_index + 1, len(nums) - 1)            
            if result != -1:
                right_index = result
            #print(result)
        #print(right_index)

        result = index
        while result != -1:
            result = self.binarySearch(nums, target, 0, left_index - 1)            
            if result != -1:
                left_index = result
            #print(result)
        #print(left_index)

        return [left_index, right_index]


    def binarySearch(self, nums: List[int], target: int, low, high) -> int:
        index = -1
        while low <= high:
            mid = int((low + high)/2)

            if nums[mid] == target:
                index = mid
                break
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return index

ob = Solution()
nums = [5,7,7,8,10]
target = 8
print(ob.searchRange(nums, target))