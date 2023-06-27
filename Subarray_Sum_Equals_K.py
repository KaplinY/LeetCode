class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        subbarray = 0
        dict = {0:1}
        for i in nums:
            subbarray += i
            cutoff = subbarray - k
            res += dict.get(cutoff,0)
            dict[subbarray] = dict.get(subbarray, 0) + 1
        return(res)


