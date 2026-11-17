class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = 10**9

        cost = [[INF] * (n + 1) for _ in range(n)]

        for i in range(n):
            for j in range(i + 2, n + 1):
                length = j - i
                best = INF

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    for r in range(d):
                        left = i + r
                        right = i + r + ((length - 1 - r) // d) * d

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1
                            left += d
                            right -= d

                    best = min(best, changes)

                cost[i][j] = best

        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for p in range(1, k + 1):
            for i in range(2 * p, n + 1):
                for j in range(2 * (p - 1), i - 1):
                    if dp[p - 1][j] != INF:
                        dp[p][i] = min(
                            dp[p][i],
                            dp[p - 1][j] + cost[j][i]
                        )

        return dp[k][n]
