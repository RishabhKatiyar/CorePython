class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        max_length_so_far = -1
        result_indexes = tuple()
        for i in range(length):
            result1 = self.expand(s, i, i)
            result2 = self.expand(s, i, i+1)
            result = result1 if result1[1] - result1[0] > result2[1] - result2[0] else result2
            if max_length_so_far < result[1] - result[0]:
                max_length_so_far = result[1] - result[0]
                result_indexes = result
        return s[result_indexes[0]:result_indexes[1]]

    def expand(self, s: str, start: int, end: int) -> tuple:
        length = len(s)
        while start >= 0 and end < length and s[start] == s[end]:
            start -= 1
            end += 1
        return (start+1, end)

s = "bb"
s = "cbbd"
s = "a"
s = "ac"
s = "babad"
ob = Solution()
print(ob.longestPalindrome(s))