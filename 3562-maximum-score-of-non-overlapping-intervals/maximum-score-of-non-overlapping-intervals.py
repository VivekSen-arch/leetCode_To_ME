class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:

        from bisect import bisect_left

        n = len(intervals)

        arr = []

        for i in range(n):
            arr.append([
                intervals[i][0],
                intervals[i][1],
                intervals[i][2],
                i
            ])

        arr.sort(key=lambda x: x[1])

        ends = []

        for x in arr:
            ends.append(x[1])

        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(1, n + 1):

            l = arr[i - 1][0]
            w = arr[i - 1][2]
            idx = arr[i - 1][3]

            p = bisect_left(ends, l, 0, i - 1)

            for j in range(1, 5):

                skip = dp[i - 1][j]

                take_score = dp[p][j - 1][0] + w
                take_indices = tuple(sorted(dp[p][j - 1][1] + (idx,)))

                if take_score > skip[0]:
                    dp[i][j] = (take_score, take_indices)

                elif take_score < skip[0]:
                    dp[i][j] = skip

                else:
                    if take_indices < skip[1]:
                        dp[i][j] = (take_score, take_indices)
                    else:
                        dp[i][j] = skip

        ans = ()

        for j in range(5):
            if dp[n][j][0] > dp[n][0][0]:
                ans = dp[n][j][1]
            elif dp[n][j][0] == dp[n][0][0]:
                if dp[n][j][1] < ans:
                    ans = dp[n][j][1]

        return list(ans)