class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        n = len(nums)
        c = [[0] * n for _ in range(n)]
        mod = 10**9 + 7
        for i in range(n):
            for j in range(i + 1):
                if j == 0:
                    c[i][j] = 1
                elif j + j > i:
                    c[i][j] = c[i][i - j]
                else:
                    c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % mod
        return (self.dfs(nums, c, mod) - 1 + mod) % mod

    def dfs(self, nums, c, mod):
        if not nums:
            return 1
        root = nums[0]
        left = []
        right = []
        for num in nums[1:]:
            if num < root:
                left.append(num)
            else:
                right.append(num)
        l_res = self.dfs(left, c, mod)
        r_res = self.dfs(right, c, mod)
        res = 1
        res = res * l_res % mod
        res = res * r_res % mod
        res = res * c[len(nums) - 1][len(left)] % mod
        return res