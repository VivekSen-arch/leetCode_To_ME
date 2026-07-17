class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1
        divCnt = [0] * (mx + 1)
        for d in range(1, mx + 1):
            for m in range(d, mx + 1, d):
                divCnt[d] += freq[m]
        exact = [0] * (mx + 1)
        for d in range(mx, 0, -1):
            pairs = divCnt[d] * (divCnt[d] - 1) // 2
            for m in range(d * 2, mx + 1, d):
                pairs -= exact[m]
            exact[d] = pairs
        prefix = [0] * (mx + 1)
        for d in range(1, mx + 1):
            prefix[d] = prefix[d - 1] + exact[d]
        ans = []
        for q in queries:
            ans.append(bisect_right(prefix, q))
        return ans