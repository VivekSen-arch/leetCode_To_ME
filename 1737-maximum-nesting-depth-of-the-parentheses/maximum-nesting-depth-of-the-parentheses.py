class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        curr_depth = 0
        for para in s:
            if para == "(":
                curr_depth += 1
                max_depth = max(max_depth, curr_depth)
            elif para == ")":
                curr_depth -= 1
        return max_depth