class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:

        n = len(s)

        # node = [left_char, right_char, prefix, suffix, best, length]
        tree = [None] * (4 * n)

        def merge(left, right):
            if left is None:
                return right

            if right is None:
                return left

            lc, lrc, lp, ls, lb, llen = left
            rc, rrc, rp, rs, rb, rlen = right

            same = (lrc == rc)

            # Prefix
            prefix = lp

            if same and lp == llen:
                prefix = llen + rp

            # Suffix
            suffix = rs

            if same and rs == rlen:
                suffix = rlen + ls

            # Best answer inside this segment
            best = max(lb, rb)

            if same:
                best = max(best, ls + rp)

            return [
                lc,
                rrc,
                prefix,
                suffix,
                best,
                llen + rlen
            ]

        def build(node, start, end):
            if start == end:
                tree[node] = [
                    s[start],
                    s[start],
                    1,
                    1,
                    1,
                    1
                ]
                return

            mid = (start + end) // 2

            build(node * 2, start, mid)
            build(node * 2 + 1, mid + 1, end)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, start, end, index, char):
            if start == end:
                tree[node] = [
                    char,
                    char,
                    1,
                    1,
                    1,
                    1
                ]
                return

            mid = (start + end) // 2

            if index <= mid:
                update(node * 2, start, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, end, index, char)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        # Build segment tree
        build(1, 0, n - 1)

        ans = []

        # Process every query
        for i in range(len(queryCharacters)):

            update(
                1,
                0,
                n - 1,
                queryIndices[i],
                queryCharacters[i]
            )

            # tree[1][4] = best
            ans.append(tree[1][4])

        return ans