class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        dp = {(0, 0): 1}
        for x in nums:
            ndp = dp.copy()
            for (a1, a2), cnt in dp.items():
                na1 = gcd(a1, x)
                ndp[(na1, a2)] = (ndp.get((na1, a2), 0) + cnt) % MOD
                na2 = gcd(a2, x)
                ndp[(a1, na2)] = (ndp.get((a1, na2), 0) + cnt) % MOD
            dp = ndp
        ans = 0
        for (a1, a2), cnt in dp.items():
            if a1 == a2 and a1 != 0:
                ans = (ans + cnt) % MOD
        return ans