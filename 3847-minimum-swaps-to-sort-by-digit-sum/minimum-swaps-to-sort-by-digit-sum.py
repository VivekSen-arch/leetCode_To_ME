
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total

        arr = sorted(nums, key=lambda x: (digit_sum(x), x))
        n = len(nums)
        pos = {v: i for i, v in enumerate(nums)}
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i]:
                continue

            cycle = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = pos[arr[j]]
                cycle += 1

            if cycle > 1:
                swaps += cycle - 1

        return swaps
