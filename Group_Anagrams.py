class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in strs:
            m = sorted(i)
            m = ''.join(m)
            if m in anagrams:
                anagrams[m].append(i)
            else:
                anagrams[m] = []
                anagrams[m].append(i)
        result = []
        for i in anagrams:
            result.append(anagrams[i])
        return(result)
        

    