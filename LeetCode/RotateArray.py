from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = k % length
        count = 0
        temp1 = nums[i-(k%length)]
        temp2 = None
        while count != length:
            count += 1
            temp2 = nums[i]
            nums[i] = temp1
            temp1 = temp2
            i += k
            if i >= length:
                i = i % length

        print(nums)

ob = Solution()

nums = [-1,-100,3,99]
k = 2
ob.rotate(nums, k)