class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        hasOdd = False
        hasEven = False
        for x in nums1:
            if x % 2 == 0:
                hasEven = True
            else:
                hasOdd = True
        if not hasOdd or not hasEven:
            return True
        return min(nums1) % 2 == 1