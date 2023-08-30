class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numbers = {}
        number = 1
        for i in nums:
            if i in numbers:
                numbers[i] = numbers[i]+1
            else:
                numbers[i] = number
        for i in numbers:
            if numbers[i] > len(nums)//2:
                return(i)