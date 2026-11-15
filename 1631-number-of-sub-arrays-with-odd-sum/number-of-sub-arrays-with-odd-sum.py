class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        odd = 0
        even = 1
        ans = 0
        prefix = 0

        for num in arr:
            prefix += num

            if prefix % 2:
                ans += even
                odd += 1
            else:
                ans += odd
                even += 1

        return ans % MOD