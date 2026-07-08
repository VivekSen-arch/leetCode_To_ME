class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)
        pref_sum = [0] * (n + 1)
        pref_nz = [0] * (n + 1)
        digits = []
        for i, ch in enumerate(s):
            d = ord(ch) - ord('0')
            pref_sum[i + 1] = pref_sum[i] + d
            pref_nz[i + 1] = pref_nz[i] + (d != 0)
            if d != 0:
                digits.append(d)
        m = len(digits)
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
        pref_val = [0] * (m + 1)
        for i in range(m):
            pref_val[i + 1] = (pref_val[i] * 10 + digits[i]) % MOD
        ans = []
        for l, r in queries:
            digit_sum = pref_sum[r + 1] - pref_sum[l]
            left = pref_nz[l]
            right = pref_nz[r + 1]
            if left == right:
                ans.append(0)
                continue
            length = right - left
            x = (pref_val[right] - pref_val[left] * pow10[length]) % MOD
            ans.append((x * digit_sum) % MOD)
        return ans