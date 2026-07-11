class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        ans = ""
        temp = strs[0]
        for i in range(0, len(temp)):
            for word in strs[1:]:
                if i == len(word) or word[i] != temp[i]:
                    return ans
            ans += temp[i]
        return ans