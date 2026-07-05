class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) 
        temp = []
        for i in range(0, n):
            if nums[i] != 0:
                temp.append(nums[i])
        a = len(temp)
        for i in range(0, a):
            nums[i] = temp[i]
        for i in range(a, n):
            nums[i] = 0