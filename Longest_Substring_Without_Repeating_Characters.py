class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result=0
        saw = {}
        left = 0

        for right in range(len(s)):
            if s[right] not in saw:
                result = max(result, right-left+1)
            else:
                if saw[s[right]] < left:
                    result = max(result, right - left + 1)
                else:
                    left = saw[s[right]] + 1
            saw[s[right]] = right
        return(result)
          



