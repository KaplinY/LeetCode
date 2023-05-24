class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dd = abs(dividend)
        dv = abs(divisor)
        result = len(range(0,dd-dv+1,dv))
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            result = -result
        l1 = -(2**31)
        l2 = 2**31-1
        if result > 0:
            result = min(result, l2)
        else:
            result = max(result, l1)
        return(result)