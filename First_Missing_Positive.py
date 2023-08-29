class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [ele for ele in nums if ele > 0] 
        nums = set(nums)
        nums = list(nums)
        nums = sorted(nums)
        if len(nums) == 1:
            if nums == [1]:
                return(2)
            else:
                return(1)
        for i in range(1,len(nums)+1):
            if nums[i-1] != i:
                return(i)
        return(len(nums)+1)