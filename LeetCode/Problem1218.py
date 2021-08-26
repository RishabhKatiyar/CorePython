from typing import List

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        max_so_far = -1
        length = len(arr)
        my_dict = {}
        for i in range(length):
            if arr[i] in my_dict:
                my_dict[arr[i]].add(i)
            else:
                my_dict[arr[i]] = {i}
        
        subsequence_length = 0
        for i in range(length):
            #print(arr[i])
            subsequence_length += 1
            next_num = arr[i] + difference
            j = i
            while next_num in my_dict:
                #print(next_num)
                val = my_dict[next_num]
                #print(val)
                flag = False
                for index in val:
                    if index > j:
                        flag = True
                        j = index
                        break
                if flag:
                    subsequence_length += 1
                    next_num += difference
                else:
                    break
            
            if max_so_far < subsequence_length:
                max_so_far = subsequence_length
            
            subsequence_length = 0
        
        return max_so_far

ob = Solution()

arr = [1,2,3,4]
difference = 1
print(ob.longestSubsequence(arr, difference))

arr = [1,3,5,7]
difference = 1
print(ob.longestSubsequence(arr, difference))

arr = [1,5,7,8,5,3,4,2,1]
difference = -2
print(ob.longestSubsequence(arr, difference))