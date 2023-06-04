class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 1:
            if citations[0] != 0:
                return(1)
            else:
                return(0)
        for i in range(1,len(citations)+2):
            res = sum(1 for j in citations if j>=i)
            if i>res:
                return(i-1)

        return(0)