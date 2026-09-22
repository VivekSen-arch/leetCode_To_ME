class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)

        tree = [[0] * k for _ in range(4 * n)]
        product = [1] * (4 * n)

        def build(node, left, right):
            if left == right:
                r = nums[left] % k
                product[node] = r
                tree[node][r] = 1
                return

            mid = (left + right) // 2

            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            L = node * 2
            R = node * 2 + 1

            product[node] = (product[L] * product[R]) % k

            for x in range(k):
                tree[node][x] = tree[L][x]

            for x in range(k):
                r = (product[L] * x) % k
                tree[node][r] += tree[R][x]

        def update(node, left, right, idx, value):
            if left == right:
                r = value % k
                product[node] = r

                for x in range(k):
                    tree[node][x] = 0

                tree[node][r] = 1
                return

            mid = (left + right) // 2

            if idx <= mid:
                update(node * 2, left, mid, idx, value)
            else:
                update(node * 2 + 1, mid + 1, right, idx, value)

            L = node * 2
            R = node * 2 + 1

            product[node] = (product[L] * product[R]) % k

            for x in range(k):
                tree[node][x] = tree[L][x]

            for x in range(k):
                r = (product[L] * x) % k
                tree[node][r] += tree[R][x]

        def query(node, left, right, ql, qr):
            if ql <= left and right <= qr:
                return product[node], tree[node][:]

            mid = (left + right) // 2

            if qr <= mid:
                return query(node * 2, left, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, right, ql, qr)

            p1, c1 = query(node * 2, left, mid, ql, qr)
            p2, c2 = query(node * 2 + 1, mid + 1, right, ql, qr)

            p = (p1 * p2) % k
            count = [0] * k

            for x in range(k):
                count[x] += c1[x]

            for x in range(k):
                r = (p1 * x) % k
                count[r] += c2[x]

            return p, count

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:
            update(1, 0, n - 1, index, value)

            _, count = query(1, 0, n - 1, start, n - 1)

            ans.append(count[x])

        return ans