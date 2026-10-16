class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        size = 1
        while size < n:
            size *= 2

        tree = [0] * (2 * size)
        lazy = [0] * (2 * size)
        ans = 0

        def update(node, start, end, left, right, val):
            if left <= start and end <= right:
                tree[node] += val * (end - start + 1)
                lazy[node] += val
                return

            mid = (start + end) // 2
            if lazy[node]:
                for child in (node * 2, node * 2 + 1):
                    length = mid - start + 1 if child == node * 2 else end - mid
                    tree[child] += lazy[node] * length
                    lazy[child] += lazy[node]
                lazy[node] = 0

            if left <= mid:
                update(node * 2, start, mid, left, right, val)
            if right > mid:
                update(node * 2 + 1, mid + 1, end, left, right, val)

            tree[node] = tree[node * 2] + tree[node * 2 + 1]

        def query(node, start, end, left, right):
            if left <= start and end <= right:
                return tree[node]

            mid = (start + end) // 2
            if lazy[node]:
                for child in (node * 2, node * 2 + 1):
                    length = mid - start + 1 if child == node * 2 else end - mid
                    tree[child] += lazy[node] * length
                    lazy[child] += lazy[node]
                lazy[node] = 0

            result = 0
            if left <= mid:
                result += query(node * 2, start, mid, left, right)
            if right > mid:
                result += query(node * 2 + 1, mid + 1, end, left, right)
            return result

        last = {}

        for i, x in enumerate(nums):
            p = last.get(x, -1)
            update(1, 0, size - 1, p + 1, i, 1)

            s = query(1, 0, size - 1, 0, i)
            ans = (ans + s) % MOD
            ans = (ans + 0) % MOD
            last[x] = i

        return self._solve(nums)

    def _solve(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        size = 1
        while size < n:
            size *= 2

        sum1 = [0] * (2 * size)
        sum2 = [0] * (2 * size)
        lazy = [0] * (2 * size)
        last = {}
        ans = 0

        def apply(node, length, val):
            sum2[node] = (sum2[node] + 2 * val * sum1[node]
                          + val * val * length) % MOD
            sum1[node] = (sum1[node] + val * length) % MOD
            lazy[node] = (lazy[node] + val) % MOD

        def push(node, start, end):
            if lazy[node] and start != end:
                mid = (start + end) // 2
                apply(node * 2, mid - start + 1, lazy[node])
                apply(node * 2 + 1, end - mid, lazy[node])
                lazy[node] = 0

        def update(node, start, end, left, right):
            if left <= start and end <= right:
                apply(node, end - start + 1, 1)
                return
            push(node, start, end)
            mid = (start + end) // 2
            if left <= mid:
                update(node * 2, start, mid, left, right)
            if right > mid:
                update(node * 2 + 1, mid + 1, end, left, right)
            sum1[node] = (sum1[node * 2] + sum1[node * 2 + 1]) % MOD
            sum2[node] = (sum2[node * 2] + sum2[node * 2 + 1]) % MOD

        for i, x in enumerate(nums):
            update(1, 0, size - 1, last.get(x, -1) + 1, i)
            ans = (ans + sum2[1]) % MOD
            last[x] = i

        return ans
