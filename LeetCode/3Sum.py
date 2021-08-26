from itertools import combinations 
import time

class Solution:
    #def threeSum(self, nums: List[int]) -> List[List[int]]:
    def threeSum(self, nums):
        result = set()
        
        nums.sort()
        negatives = []
        positives = []
        zeroes = []

        for num in nums:
            if num < 0:
                negatives.append(num)
            elif num > 0:
                positives.append(num)
            else:
                zeroes.append(num)

        if len(zeroes) >= 3:
            result.add(tuple([0,0,0]))

        length = len(negatives)
        for i in range(length):
            for j in range(i+1, length):
                positive = (negatives[i] + negatives[j]) * -1
                # binary search

                index = -1
                low = 0 
                high = len(positives) - 1
                
                while low <= high:
                    mid = int((high + low) / 2)
                    if positives[mid] == positive:
                        index = mid
                        break
                    if positives[mid] < positive:
                        low = mid + 1
                    else:
                        high = mid - 1
                

                if index != -1:
                    result.add(tuple([negatives[i], negatives[j], positive]))

        length = len(positives)
        for i in range(length):
            for j in range(i+1, length):
                negative = (positives[i] + positives[j]) * -1
                 # binary search

                index = -1
                low = 0 
                high = len(negatives) - 1
                
                while low <= high:
                    mid = int((high + low) / 2)
                    if negatives[mid] == negative:
                        index = mid
                        break
                    if negatives[mid] < negative:
                        low = mid + 1
                    else:
                        high = mid - 1

                if index != -1:
                    result.add(tuple([positives[i], positives[j], negative]))
        
        if len(zeroes) != 0:
            for negative in negatives:
                # binary search

                index = -1
                low = 0 
                high = len(positives) - 1
                positive = negative * -1
                while low <= high:
                    mid = int((high + low) / 2)
                    if positives[mid] == positive:
                        index = mid
                        break
                    if positives[mid] < positive:
                        low = mid + 1
                    else:
                        high = mid - 1

                if index != -1:
                    result.add(tuple([negative, 0, negative*-1]))

        return result


if __name__ == '__main__':
    ls = input()
    nums = ls.split(',')
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    # nums=[]
    tsum = Solution()
    start = time.perf_counter()

    results = tsum.threeSum(list(nums))

    end = time.perf_counter()
    for ls in results:
        print(ls)

    print(f'Time taken = {end - start}')