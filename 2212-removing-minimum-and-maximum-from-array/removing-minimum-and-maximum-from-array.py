class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        if min_idx > max_idx:
            min_idx, max_idx = max_idx, min_idx
        front = max_idx + 1
        back = n - min_idx
        both = min_idx + 1 + n - max_idx
        return min(front, back, both)