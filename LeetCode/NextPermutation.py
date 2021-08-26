from typing import List
from itertools import permutations
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = nums.copy()
        temp.sort()
        perm = permutations(temp, len(nums))
        perm_list = list(perm)
        print(set(perm_list))
        length = len(perm_list)
        i = 0
        while i < length:
            are_equal = True
            permutation = list(perm_list[i])
            #print(permutation)
            #print(nums)
            for j in range(len(nums)):
                if permutation[j] != nums[j]:
                    are_equal = False
                    break
            if are_equal:
                break
            i += 1
        
        #print(i)
        index_to_copy = i + 1
        if index_to_copy == length:
            index_to_copy = 0
        
        result_list = perm_list[index_to_copy]
        #print(result_list)
        index = 0
        for i in result_list:
            nums[index] = i
            index += 1
        print(nums)


ob = Solution()
nums = [1,5,1]
ob.nextPermutation(nums)
#print(nums)