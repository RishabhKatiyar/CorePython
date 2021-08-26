from itertools import permutations

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        num = str(n)
        flag = False
        length = len(num)
        for i in range(length-1):
            if num[i] < num[i+1]:
                flag = True
                break
        if not flag:
            return -1
        digits = []
        temp = n
        while temp != 0:
            digits.append(str(temp % 10))
            temp = int(temp/10)
        digits.sort()
        res = permutations(digits)
        for item in res:
            result = int(''.join(item))
            if result > n:
                break
        if result > (2**31)-1:
            return -1
        return result


ob = Solution()
print(ob.nextGreaterElement(22))
print(ob.nextGreaterElement(12))
print(ob.nextGreaterElement(198765432))

