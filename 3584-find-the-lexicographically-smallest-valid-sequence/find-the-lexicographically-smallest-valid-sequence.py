from typing import List
from bisect import bisect_left

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)

        pos = [[] for _ in range(26)]

        for i, ch in enumerate(word1):
            pos[ord(ch) - 97].append(i)

        suf0 = [-1] * (m + 1)
        suf1 = [-1] * (m + 1)

        suf0[m] = n
        suf1[m] = n

        prev_diff = [-1] * n

        last = [-1] * 26
        best1 = best2 = -1
        char1 = char2 = -1

        for i, ch in enumerate(word1):
            c = ord(ch) - 97

            if char1 != c:
                prev_diff[i] = best1
            else:
                prev_diff[i] = best2

            if char1 == c:
                best1 = i
            elif char2 == c:
                best2 = i
            elif i > best1:
                best2, char2 = best1, char1
                best1, char1 = i, c
            elif i > best2:
                best2, char2 = i, c

        for i in range(m - 1, -1, -1):
            c = ord(word2[i]) - 97
            arr = pos[c]

            k = bisect_left(arr, suf0[i + 1])

            if k > 0:
                suf0[i] = arr[k - 1]

            k = bisect_left(arr, suf1[i + 1])

            exact = -1

            if k > 0:
                exact = arr[k - 1]

            bound = suf0[i + 1]
            different = -1

            if bound > 0:
                p = bound - 1

                if word1[p] != word2[i]:
                    different = p
                else:
                    different = prev_diff[p]

            suf1[i] = max(exact, different)

        ans = []
        prev = -1
        used = False

        for i in range(m):
            j = prev + 1
            found = -1

            while j < n and j < max(suf0[i + 1], suf1[i + 1]):
                if word1[j] == word2[i]:
                    if j < suf1[i + 1]:
                        found = j
                        break
                elif not used:
                    if j < suf0[i + 1]:
                        found = j
                        break

                j += 1

            if found == -1:
                return []

            if word1[found] != word2[i]:
                used = True

            ans.append(found)
            prev = found

        return ans