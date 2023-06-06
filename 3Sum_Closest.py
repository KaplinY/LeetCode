class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums,reverse=False)
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
                left = i+1
                right = len(nums)-1
                while left<right:
                    sum = nums[i]+nums[left]+nums[right]
                    if abs(result-target) > abs(sum-target):
                        result = sum
                    if sum == target:
                        break
                    elif sum<target:
                        left+=1
                    else:
                        right-=1
        return(result)