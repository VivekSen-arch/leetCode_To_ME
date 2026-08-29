class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        arr = sorted((value, index) for index, value in enumerate(nums))

        i = 0

        while i < len(nums):
            j = i

            while j + 1 < len(nums) and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            indices = sorted(arr[k][1] for k in range(i, j + 1))

            for k in range(len(indices)):
                nums[indices[k]] = arr[i + k][0]

            i = j + 1

        return nums