class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]
        dp = [[0] * (n + 1) for _ in range(n)]
        def solve(i, m):
            if i >= n:
                return 0
            if dp[i][m] != 0:
                return dp[i][m]
            best = 0
            for x in range(1, 2 * m + 1):
                if i + x > n:
                    break
                opponent = solve(i + x, max(m, x))
                best = max(best, suffix[i] - opponent)
            dp[i][m] = best
            return best
        return solve(0,  1)