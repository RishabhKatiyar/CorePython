class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0 :
            return 0
        is_negative = False
        if dividend < 0  and divisor < 0:
            pass
        elif dividend < 0 or divisor < 0:
            is_negative = True
        

        dividend = abs(dividend)
        divisor = abs(divisor)

        if dividend == divisor:
            result = 1 if not is_negative else -1
            return result
        
        if divisor == 1:
            result = dividend if not is_negative else -dividend
            if result > (1<<31)-1 or result < -1<<31:
                result = (1<<31)-1
            return result

        result = 0

        for i in range(divisor, dividend, divisor):
            result += 1

        result = result if not is_negative else -result
        
        if result > (1<<31)-1 or result < -1<<31:
            result = (1<<31)-1
        
        return result
        

ob = Solution()
print(ob.divide(10, 3))
print(ob.divide(7, -3))
print(ob.divide(0, 1))
print(ob.divide(1, 1))
print(ob.divide(2, 1))
print(ob.divide(2, -2))
print(ob.divide(-2147483648, -1))