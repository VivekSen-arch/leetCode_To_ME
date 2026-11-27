
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        min_price = min(price for factor, price in items)

        values = []

        for i in range(n):
            free = 0

            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    free += 1

            values.append(1 + free)

        dp = [-10**9] * (budget + 1)
        dp[0] = 0

        for i in range(n):
            price = items[i][1]
            value = values[i]

            for c in range(budget, price - 1, -1):
                dp[c] = max(dp[c], dp[c - price] + value)

        ans = 0

        for c in range(budget + 1):
            if dp[c] >= 0:
                ans = max(ans, dp[c] + (budget - c) // min_price)

        return ans
