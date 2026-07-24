class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        MAXX = 2048
        vals = list(set(nums))
        dp = [[False] * MAXX for _ in range(4)]
        dp[0][0] = True
        for k in range(3):
            for x in range(MAXX):
                if dp[k][x]:
                    for v in vals:
                        dp[k + 1][x ^ v] = True
        return sum(dp[3])