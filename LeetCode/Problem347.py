class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        tuple_list = list(dict.items())
        tuple_list.sort(key = lambda item: item[1])
        length = len(tuple_list)
        result = []
        count = 0
        for i in range(length-1, -1, -1):
            item = tuple_list[i]
            result.append(item[0])
            count += 1
            if count == k:
                break
        return result

nums = [1,1,1,2,2,3]
k = 2
ob = Solution()
print(ob.topKFrequent(nums, k))