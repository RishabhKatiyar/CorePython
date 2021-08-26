class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = len(s)
        char_count = [0] * 26
        max_char_count = 0
        start = 0
        max_so_far = 0
        for i in range(length):
            index = ord(s[i]) - ord('A')
            char_count[index] += 1
            max_char_count = max(char_count[index], max_char_count)
            if i - start + 1 - max_char_count > k:
                index = ord(s[start]) - ord('A')
                char_count[index] -= 1
                if max_so_far < i - start:
                    max_so_far = i - start
                start += 1
        if max_so_far < i - start + 1:
            max_so_far = i - start + 1
        return max_so_far

s = "ABC" 
s = "AABABB"
#s = "AABABBA"
#s = "ABAB"
k = 3
ob = Solution()
print(ob.characterReplacement(s, k))