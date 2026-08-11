class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break
        s = set(nums)
        while total in s:
            total += 1
        return total 