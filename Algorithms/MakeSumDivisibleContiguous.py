
class Solution:
    def minSubarray(self, nums, p):
        sum = 0
        for num in nums:
            sum = sum + num
        if p > sum:
            return -1
            
        rem = sum % p
        if rem == 0:
            return 0
        
        length = len(nums)
        
        start = -1
        sum = 0
        min_len = None
        
        for i in range(length):
            current = nums[i]
            if current > rem:
                start = -1
                sum = 0
            elif current == rem:
                return 1
            elif current < rem:
                temp_sum = current + sum
                if temp_sum < rem:
                    if start == -1:
                        start = i
                    sum = sum + current
                elif temp_sum == rem:
                    if min_len is None:
                        min_len = i - start
                    elif min_len > i - start:
                        min_len = i - start
                    start = i
                    sum = current
                elif temp_sum > rem:
                    start = i
                    sum = current

        if min_len is not None:
            return min_len + 1            
        return -1

if __name__ == '__main__':
    ls = input()
    nums = [int(x) for x in ls.split(',')]
    p = int(input())
    
    obj = Solution()
    res = obj.minSubarray(nums, p)

    print(res)