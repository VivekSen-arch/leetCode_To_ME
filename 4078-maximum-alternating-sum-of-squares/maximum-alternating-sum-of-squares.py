class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=abs, reverse = True)
        n = len(nums)
        k = (n+ 1) // 2
        ans = 0
        for i in range(k):
            ans += nums[i] * nums[i]
        for i in range(k, n):
            ans -= nums[i] * nums[i]
        return ans