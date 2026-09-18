class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}

        for i in range(len(s)):
            if s[i] not in first:
                first[s[i]] = i
            last[s[i]] = i

        intervals = []

        for ch in first:
            l = first[ch]
            r = last[ch]
            i = l
            valid = True

            while i <= r:
                c = s[i]

                if first[c] < l:
                    valid = False
                    break

                r = max(r, last[c])
                i += 1

            if valid:
                intervals.append((l, r))

        intervals.sort(key=lambda x: x[1])

        ans = []
        end = -1

        for l, r in intervals:
            if l > end:
                ans.append(s[l:r + 1])
                end = r

        return ans