class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        number = 2**k
        flag = True
        for i in range(number):
            temp = format(i, "b")
            substring = "0" * (k - len(temp)) + temp
            if s.find(substring) == -1:
                flag = False
                break
        return flag


ob = Solution()
s = "00110"
k = 2
print(ob.hasAllCodes(s, k))

s = "0110"
k = 2
print(ob.hasAllCodes(s, k))