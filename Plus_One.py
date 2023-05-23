class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = 0
        n = len(digits)
        for i in digits:
            integer = integer + i*(10**(n-1))
            n -= 1
        integer += 1
        res = [int(x) for x in str(integer)]
        return(res)