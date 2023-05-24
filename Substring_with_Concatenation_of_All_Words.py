import textwrap
import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordlen = len(words[0])
        window = len(words[0])*len(words)
        words = Counter(words)
        result =[]
        if window > len(s):
            return(result)
        for i in range(len(s)-window+1):
            substr = s[i:window+i]
            substr = textwrap.wrap(substr,wordlen)
            substr = Counter(substr)
            if substr == words:
                result.append(i)
        return(result)



