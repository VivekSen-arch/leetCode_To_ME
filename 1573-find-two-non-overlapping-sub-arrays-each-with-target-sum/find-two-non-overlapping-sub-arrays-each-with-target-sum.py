class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        inf = n + 1
        
        best = [inf] * n
        
        left = 0
        curr_sum = 0
        min_len = inf
        ans = inf
        
        for right in range(n):
            curr_sum += arr[right]
            
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1
            
            if curr_sum == target:
                length = right - left + 1
                
                if left > 0 and best[left - 1] != inf:
                    ans = min(ans, length + best[left - 1])
                
                min_len = min(min_len, length)
            
            if right == 0:
                best[right] = min_len
            else:
                best[right] = min(best[right - 1], min_len)
        
        if ans == inf:
            return -1
        
        return ans