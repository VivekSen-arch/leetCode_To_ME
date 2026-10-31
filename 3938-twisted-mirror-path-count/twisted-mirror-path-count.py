class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        memo = {}

        def jump(r, c, d):
            path = []

            while 0 <= r < m and 0 <= c < n:
                if grid[r][c] == 0:
                    res = (r, c)
                    break

                key = (r, c, d)

                if key in memo:
                    res = memo[key]
                    break

                path.append(key)

                if d == 0:
                    r += 1
                    d = 1
                else:
                    c += 1
                    d = 0
            else:
                res = None

            for key in path:
                memo[key] = res

            return res

        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    continue

                if i == m - 1 and j == n - 1:
                    continue

                for dr, dc, d in [(0, 1, 0), (1, 0, 1)]:
                    nxt = jump(i + dr, j + dc, d)

                    if nxt is not None:
                        x, y = nxt
                        dp[x][y] = (dp[x][y] + dp[i][j]) % MOD

        return dp[m - 1][n - 1]