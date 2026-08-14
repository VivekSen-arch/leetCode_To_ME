class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = defaultdict(int)
        left = 0
        max_len = 0
        for right, char in enumerate(s):
            count[char] += 1
            while count[char] > 2:
                count[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len 