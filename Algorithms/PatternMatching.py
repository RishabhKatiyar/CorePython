class Solution:
    def StringChallenge(self, strParam):
        pattern, text = strParam.split()
        p_len = len(pattern)
        t_len = len(text)
        flag = True
        p = 0
        t = 0
        if len(pattern) > len(text):
            return False  
        while t<len(text):
            if pattern [p] == "+" and text[t].isalpha():
                p += 1
                t += 1
            else:
                return False
            if pattern[p] == "$" and text[t].isdigit():
                p += 1
                t += 1
            else:
                return False
            if pattern[p] == "*":
                factor = 3
                if p+1 < p_len:
                    if pattern[p+1] == "{":
                        factor = pattern[p+2]
                        p += 4
                    else:
                        p += 1
                for _f in range(factor):
                    if t+f > t_len-1:
                        return False
                    if not text [t] == text[t+f]:
                        return False
                t += factor
        return True

# "$*+{2} 9mmmrrrkbb"
ob = Solution()
print(ob.StringChallenge("$*+{2} 9mmmrrrkbb"))