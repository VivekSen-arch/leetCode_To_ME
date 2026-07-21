class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')
        prev_zero = float('-inf')
        best = 0
        i = 0
        n = len(s)
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            length = j - i
            if s[i] == '1':
                pass
            else:
                best = max(best, prev_zero + length)
                prev_zero = length
            i = j
        return ones + best