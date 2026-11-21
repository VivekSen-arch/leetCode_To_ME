
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        last = [-1] * 26

        stack = [(0, False, -1)]

        while stack:
            node, exiting, old = stack.pop()
            ch = ord(s[node]) - ord('a')

            if exiting:
                last[ch] = old
                continue

            if last[ch] != -1:
                new_parent[node] = last[ch]

            old = last[ch]
            last[ch] = node

            stack.append((node, True, old))

            for child in reversed(children[node]):
                stack.append((child, False, -1))

        new_children = [[] for _ in range(n)]
        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        order = [0]
        for node in order:
            order.extend(new_children[node])

        ans = [1] * n

        for node in reversed(order):
            if node != 0:
                ans[new_parent[node]] += ans[node]

        return ans
