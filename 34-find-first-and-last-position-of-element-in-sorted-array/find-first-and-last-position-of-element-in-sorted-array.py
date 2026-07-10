class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        first = -1
        last = -1
        for i in range(0, n):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i
        return [first, last]