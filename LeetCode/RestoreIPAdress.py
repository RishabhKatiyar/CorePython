from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        queue = []
        value = s[:1]
        if self.isValid(value):
            queue.append((value + ".", 0, 0))
        value = s[:2]
        if self.isValid(value):
            queue.append((value + ".", 1, 0))
        value = s[:3]
        if self.isValid(value):
            queue.append((value + ".", 2, 0))

        while len(queue):
            item = queue.pop(0)
            level = item[2]
            index = item[1] + 1
            address = item[0]
            if level < 2:
                value = s[index:index+1]
                if self.isValid(value):
                    queue.append((address + value + ".", index+0, level + 1))
                value = s[index:index+2]
                if self.isValid(value):
                    queue.append((address + value + ".", index+1, level + 1))
                value = s[index:index+3]
                if self.isValid(value):
                    queue.append((address + value + ".", index+2, level + 1))
            else:
                value = s[index:]
                if self.isValid(value):
                    result.append(address + value)
        return result

    def isValid(self, s:str) -> bool:
        if len(s) == 0:
            return False
        if len(s) == 1:
            return True
        if s[0] == "0":
            return False
        value = int(s)
        if 0 <= value and value <= 255:
            return True
        return False

ob = Solution()
s = "25525511135"
print(ob.restoreIpAddresses(s))
s = "0000"
print(ob.restoreIpAddresses(s))
s = "1111"
print(ob.restoreIpAddresses(s))
s = "010010"
print(ob.restoreIpAddresses(s))
s = "101023"
print(ob.restoreIpAddresses(s))