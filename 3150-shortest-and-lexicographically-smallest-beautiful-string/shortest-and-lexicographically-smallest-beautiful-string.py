class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = []
        for i in range(len(s)):
            if s[i] == '1':
                ones.append(i)
        ans = ""
        for i in range(len(ones) - k + 1):
            left = ones[i]
            right = ones[i + k - 1]
            sub = s[left:right + 1]
            if ans == "":
                ans = sub
            elif len(sub) < len(ans):
                ans = sub
            elif len(sub) == len(ans) and sub < ans:
                ans = sub
        return ans 