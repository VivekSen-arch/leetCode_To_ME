class Solution:
    def romanToInt(self, s: str) -> int:
        letters = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        n = len(s)
        ans = 0
        for i in range(0, n):
            if i < n - 1 and letters[s[i]] < letters[s[i + 1]]:
                ans -= letters[s[i]]
            else:
                ans += letters[s[i]]
        return ans