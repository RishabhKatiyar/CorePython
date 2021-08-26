class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _set = set()
        max_so_far = 0
        length = len(s)
        start = 0
        for i in range(length):
            if not s[i] in _set:
                _set.add(s[i]) 
                if max_so_far < len(_set):
                    max_so_far = len(_set)              
            else:
               while s[start] != s[i]:
                   _set.remove(s[start])
                   start += 1
               start += 1 
        return max_so_far

s = ""
#s = " "
#s = "aab"
#s = ""
#s = "dvdf"
#s = "abcabcbb"
#s = "abcbbcbb"
#s = "bbbbb"
#s = "pwwkew"

ob = Solution()
print(ob.lengthOfLongestSubstring(s))