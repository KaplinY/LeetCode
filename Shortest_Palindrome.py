class Solution:
    def shortestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            if s == s[::-1]:
                return(s)
            s = s[:i] + s[len(s)-i-1] + s[i:]
        return(s)