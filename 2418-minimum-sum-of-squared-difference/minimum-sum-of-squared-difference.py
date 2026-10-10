class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        from collections import Counter

        k = k1 + k2
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]

        if sum(diff) <= k:
            return 0

        freq = Counter(diff)
        max_diff = max(diff)

        while k > 0 and max_diff > 0:
            count = freq[max_diff]
            reduce = min(k, count)

            freq[max_diff] -= reduce
            freq[max_diff - 1] += reduce
            k -= reduce

            if freq[max_diff] == 0:
                del freq[max_diff]

            max_diff -= 1

        return sum(d * d * count for d, count in freq.items())
