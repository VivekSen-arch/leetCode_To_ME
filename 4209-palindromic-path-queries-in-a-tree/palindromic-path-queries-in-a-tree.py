class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        from collections import deque

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()
        parent = [-1] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        pref = [0] * n
        timer = 0

        bit = [1 << (ord(c) - ord('a')) for c in s]

        stack = [(0, -1, 0)]
        while stack:
            u, p, state = stack.pop()

            if state == 0:
                parent[u] = p
                tin[u] = timer
                timer += 1

                pref[u] = bit[u]
                if p != -1:
                    pref[u] ^= pref[p]

                stack.append((u, p, 1))

                for v in reversed(graph[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer

        up = [[-1] * n for _ in range(LOG)]
        up[0] = parent[:]

        for k in range(1, LOG):
            for u in range(n):
                p = up[k - 1][u]
                if p != -1:
                    up[k][u] = up[k - 1][p]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            k = 0
            while diff:
                if diff & 1:
                    u = up[k][u]
                diff >>= 1
                k += 1

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]

            return parent[u]

        fenwick = [0] * (n + 2)

        def add(i, value):
            i += 1
            while i <= n:
                fenwick[i] ^= value
                i += i & -i

        def get(i):
            i += 1
            result = 0
            while i > 0:
                result ^= fenwick[i]
                i -= i & -i
            return result

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                new_bit = 1 << (ord(c) - ord('a'))
                delta = bit[u] ^ new_bit

                if delta:
                    add(tin[u], delta)
                    if tout[u] < n:
                        add(tout[u], delta)

                    bit[u] = new_bit

            else:
                u = int(parts[1])
                v = int(parts[2])

                w = lca(u, v)

                mask = pref[u] ^ get(tin[u])
                mask ^= pref[v] ^ get(tin[v])
                mask ^= bit[w]

                ans.append((mask & (mask - 1)) == 0)

        return ans