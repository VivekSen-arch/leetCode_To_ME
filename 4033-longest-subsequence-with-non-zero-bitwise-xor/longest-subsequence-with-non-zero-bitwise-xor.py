class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xr = 0
        has_nonzero = False
        for x in nums:
            xr ^= x
            if x != 0:
                has_nonzero = True
        if not has_nonzero:
            return 0
        if xr != 0:
            return len(nums)
        return len(nums) - 1