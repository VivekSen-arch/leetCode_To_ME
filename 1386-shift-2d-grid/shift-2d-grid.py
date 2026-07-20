class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        total = m * n
        k %= total
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                idx = i * n + j
                newidx = (idx + k) % total
                ans[newidx // n][newidx % n] = grid[i][j]
        return ans