class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if x < 0:
            is_negative = True
        x = abs(x)
        reverse = 0
        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x = int(x / 10)        
        x = reverse if not is_negative else -reverse
        if x > (1<<31)-1 or x < -1<<31:
            x = 0
        return x


ob = Solution()

print(ob.reverse(123))
print(ob.reverse(-123))
print(ob.reverse(120))
print(ob.reverse(-120))
print(ob.reverse(1534236469))
print(ob.reverse(1563847412))