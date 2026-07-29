from collections import Counter

class Solution:
    def __init__(self):
        self.MAX = 10 ** 6 + 1

    def smallestPalindrome(self, s: str, k: int) -> str:
        count = Counter(s)

        half = [0] * 26
        mid = ""

        for ch, freq in count.items():
            half[ord(ch) - ord("a")] = freq // 2
            if freq % 2:
                mid = ch

        if self._countWays(half) < k:
            return ""

        left = []
        length = sum(half)

        for _ in range(length):
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                ways = self._countWays(half)

                if ways >= k:
                    left.append(chr(i + ord("a")))
                    break

                k -= ways
                half[i] += 1

        left = "".join(left)
        return left + mid + left[::-1]

    def _countWays(self, cnt):
        total = sum(cnt)
        res = 1

        for x in cnt:
            if x:
                res *= self._nCr(total, x)
                if res >= self.MAX:
                    return self.MAX
                total -= x

        return res

    def _nCr(self, n, r):
        r = min(r, n - r)
        res = 1

        for i in range(1, r + 1):
            res = res * (n - i + 1) // i
            if res >= self.MAX:
                return self.MAX

        return res