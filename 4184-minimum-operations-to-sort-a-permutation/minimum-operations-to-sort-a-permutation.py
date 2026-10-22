class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        min_ops = float('inf')
        
        # Check Family 1: Rotation of [0, 1, ..., n - 1]
        k1 = nums[0]
        is_family1 = True
        for i in range(n):
            if nums[i] != (k1 + i) % n:
                is_family1 = False
                break
        
        if is_family1:
            if k1 == 0:
                ops1 = 0
            else:
                ops1 = min(n - k1, 1 + min(k1 + 1, n - k1 + 1))
            min_ops = min(min_ops, ops1)
            
        # Check Family 2: Rotation of [n - 1, n - 2, ..., 0]
        c = nums[0]
        is_family2 = True
        for i in range(n):
            if nums[i] != (c - i + n) % n:
                is_family2 = False
                break
                
        if is_family2:
            k2 = (n - 1 - c) % n
            ops2 = min(k2 + 1, n - k2 + 1)
            min_ops = min(min_ops, ops2)
            
        return min_ops if min_ops != float('inf') else -1