from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = self.func(n)
        return list(result)

    def func(self, n: int):
        if n == 1:
            return ["()"]
        else:
            result = self.func(n-1)
            result_set = set()
            for item in result:
                s = str(item)
                length = len(s)
                for i in range(1, length+2):
                    value = s[:i-1]+"()"+s[i-1:]
                    result_set.add(value)
            return result_set

ob = Solution()
print(ob.generateParenthesis(3))