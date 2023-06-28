from itertools import product
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        return (sorted(list(product(nums1,nums2)),key = lambda x: x[0] + x[1])[:k])
