class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        rev = s[::-1]
        if rev[-1] != '-':
            if int(rev) < 2147483647:
                return int(rev)
            else:
                return 0
        else:
            rev = rev.replace('-','')
            if -int(rev) > -2147483648:
                return -int(rev)
            else:
                return 0