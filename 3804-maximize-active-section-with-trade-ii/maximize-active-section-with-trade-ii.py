from typing import List
from dataclasses import dataclass
import itertools

@dataclass
class Group:
    start: int
    length: int

class SparseTable:
    def __init__(self, nums):
        n = len(nums)
        if n == 0:
            self.st = [[0]]
            return

        self.st = [nums[:]]
        k = 1
        while (1 << k) <= n:
            prev = self.st[-1]
            cur = []
            half = 1 << (k - 1)
            for i in range(n - (1 << k) + 1):
                cur.append(max(prev[i], prev[i + half]))
            self.st.append(cur)
            k += 1

    def query(self, l, r):
        if l > r:
            return 0
        k = (r - l + 1).bit_length() - 1
        return max(self.st[k][l], self.st[k][r - (1 << k) + 1])

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:

        ones = s.count('1')

        zeroGroups = []
        zeroGroupIndex = []

        for i, ch in enumerate(s):
            if ch == '0':
                if i > 0 and s[i - 1] == '0':
                    zeroGroups[-1].length += 1
                else:
                    zeroGroups.append(Group(i, 1))
            zeroGroupIndex.append(len(zeroGroups) - 1)

        if not zeroGroups:
            return [ones] * len(queries)

        merge = []
        for a, b in itertools.pairwise(zeroGroups):
            merge.append(a.length + b.length)

        st = SparseTable(merge)

        ans = []

        for l, r in queries:

            left = -1
            if zeroGroupIndex[l] != -1:
                g = zeroGroups[zeroGroupIndex[l]]
                left = g.length - (l - g.start)

            right = -1
            if zeroGroupIndex[r] != -1:
                g = zeroGroups[zeroGroupIndex[r]]
                right = r - g.start + 1

            startPair = zeroGroupIndex[l] + 1
            endGroup = zeroGroupIndex[r] if s[r] == '1' else zeroGroupIndex[r] - 1
            endPair = endGroup - 1

            best = ones

            if (
                s[l] == '0'
                and s[r] == '0'
                and zeroGroupIndex[l] + 1 == zeroGroupIndex[r]
            ):
                best = max(best, ones + left + right)

            elif startPair <= endPair:
                best = max(best, ones + st.query(startPair, endPair))

            if (
                s[l] == '0'
                and zeroGroupIndex[l] + 1 <= endGroup
            ):
                best = max(
                    best,
                    ones + left + zeroGroups[zeroGroupIndex[l] + 1].length
                )

            if (
                s[r] == '0'
                and zeroGroupIndex[l] < zeroGroupIndex[r] - 1
            ):
                best = max(
                    best,
                    ones + right + zeroGroups[zeroGroupIndex[r] - 1].length
                )

            ans.append(best)

        return ans