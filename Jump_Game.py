class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return(True)
        if nums[0] == 0:
            return(False)
        for i in range(len(nums)-1):
            if nums[i] + i >= len(nums)-1:
                return(True)
            if nums[i+1] == 0:
                n=i+1
                k=0
                if i == 0 and nums[0] != 1:
                    k+=1
                for j in range(i+1):
                    if nums[j]+j > n:
                        k+=1
                if k == 0:
                    return(False)
        return(True)