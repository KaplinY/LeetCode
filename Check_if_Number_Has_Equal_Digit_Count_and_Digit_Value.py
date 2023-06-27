class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            m = str(i)
            x=str(num.count(m))
            if x != num[i]:
                return False
        return True
