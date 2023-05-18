class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(min(strs, key = len))
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        result=""
        for i in range(length):
            if first[i]!=last[i]:
                return(result)
            else:
                result+=first[i]
        return(result)