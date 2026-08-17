from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]

        leftBest = [[0] * n for _ in range(n)]

        rightBest = [[0] * n for _ in range(n)]

        for i in range(n):
            leftBest[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                total = prefix[r + 1] - prefix[l]

                lo = l
                hi = r

                while lo < hi:
                    mid = (lo + hi) // 2

                    left = prefix[mid + 1] - prefix[l]

                    if left * 2 < total:
                        lo = mid + 1
                    else:
                        hi = mid

                k = lo

                ans = 0

                if k > l:
                    ans = max(ans, leftBest[l][k - 1])

                if k < r:
                    left = prefix[k + 1] - prefix[l]
                    right = total - left

                    if left < right:
                        ans = max(
                            ans,
                            left + dp[l][k]
                        )

                    elif left > right:
                        ans = max(
                            ans,
                            right + dp[k + 1][r]
                        )

                    else:
                        ans = max(
                            ans,
                            left + dp[l][k],
                            right + dp[k + 1][r]
                        )

                    if k + 1 < r:
                        ans = max(
                            ans,
                            rightBest[k + 1][r]
                        )

                dp[l][r] = ans

                current_left = total + dp[l][r]

                leftBest[l][r] = max(
                    leftBest[l][r - 1],
                    current_left
                )

                current_right = (
                    prefix[r + 1]
                    - prefix[l + 1]
                    + dp[l + 1][r]
                )

                rightBest[l][r] = max(
                    current_right,
                    rightBest[l + 1][r]
                )

        return dp[0][n - 1]