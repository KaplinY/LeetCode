class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2
        if nums[mid] == target or mid<1:
            if nums[mid] < target:
                return 1
            return mid
        if target > nums[mid]:
            return mid+self.searchInsert(nums[mid:],target)
        if target < nums[mid]:
            return self.searchInsert(nums[:mid],target)