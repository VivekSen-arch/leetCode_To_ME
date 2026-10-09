class Solution:
    def minInsertions(self, s: str) -> int:
        i = 0
        n = 0
        for ch in s:
            if ch == "(":
                if n % 2 == 1:
                    i += 1
                    n -= 1
                n += 2
            else:
                n -= 1
                if n < 0:
                    i += 1
                    n = 1
        return i + n