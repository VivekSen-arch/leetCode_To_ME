class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k
        for num in nums:
            new  = [0] * k
            r = num % k
            new[r] += 1
            for i in range(k):
                if dp[i] > 0:
                    new[(i * r) % k] += dp[i]
            for i in range(k):
                ans[i] += new[i]
            dp = new
        return ans 