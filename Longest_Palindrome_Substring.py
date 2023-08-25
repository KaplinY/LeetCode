class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindromes = []
        if len(s) == 1:
            return(s)
        def sliding_window(s,n):
            for i in range(len(s)-n+1):
                window = s[i:i+n]
                if window == window[::-1]:
                    palindromes.append(window)
        for i in range (1,len(s)+1):
            sliding_window(s,i)
        max_len = -1
        for ele in palindromes:
            if len(ele) > max_len:
                max_len = len(ele)
                res = ele
        return(res)


