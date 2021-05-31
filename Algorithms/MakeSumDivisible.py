
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
        
        sum_nums = []

        for num in nums:
            if num == rem:
                return 1
            if num < rem:
                sum_nums.append(num)
        nums = []

        print(f'Remainder = {rem}')
        #sum_nums.sort()
        print(sum_nums)

        count = 0
        sum = 0
        start = 0
        result = -1
        length = len(sum_nums)

        for i in range(length):
            sum = sum + sum_nums[i]
            count = count + 1
            if sum == rem:
                result = count
            if sum > rem:
                start = start + 1
                count = count -1
            if sum < rem:
                continue

        return result

if __name__ == '__main__':
    ls = input()
    nums = [int(x) for x in ls.split(',')]
    p = int(input())
    
    obj = Solution()
    res = obj.minSubarray(nums, p)

    print(res)