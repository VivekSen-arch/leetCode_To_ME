class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in a:
                return [a[diff], i]
            a[num] = i
        