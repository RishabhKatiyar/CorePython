class Solution:
    def longestPalindrome(self, s):
        length = len(s)
        result = [-1,-1]
        for i in range(length):
            #if length % 2 == 1:
            res = self.expand(s, i)
            if res[1] - res[0] > result[1] - result[0]:
                result[0] = res[0]
                result[1] = res[1]
            #else:
            if i+1 < len(s):
                if s[i] == s[i+1]:
                    res = self.expand(s, i, i+1)
                    if res[1] - res[0] > result[1] - result[0]:
                        result[0] = res[0]
                        result[1] = res[1]
        palindrome = s[result[0]:result[1]+1]
        if palindrome == '':
            palindrome = s[0]
        return palindrome

    def expand(self, s, i, j = None):
        if j is None:
            start = i - 1
            end = i + 1
        else:
            start = i - 1
            end = j + 1
        while True:
            if not (start < 0 or end >= len(s)):
                if s[start] == s[end]:
                    start = start - 1
                    end = end + 1
                else:
                    break
            else:
                break
        return (start+1, end-1)

if __name__ == '__main__':
    s = input ()
    obj = Solution()
    print(obj.longestPalindrome(s))
        