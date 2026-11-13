import collections
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        cost = 0
        dq = collections.deque()
        j = n - 1
        
        # Iterate the left endpoint `i` from right to left
        for i in range(n - 1, -1, -1):
            num = nums[i]
            
            # Maintain monotonic stack/deque of elements in non-increasing order
            while dq and nums[dq[-1]] < num:
                l = dq.pop()
                r = dq[-1] if dq else j + 1
                cost += (r - l) * (num - nums[l])
                
            dq.append(i)
            
            # If the current cost exceeds k, shrink the window from the right (decrement j)
            while cost > k:
                cost -= nums[dq[0]] - nums[j]
                if dq[0] == j:
                    dq.popleft()
                j -= 1
                
            # All subarrays starting at `i` and ending anywhere from `i` to `j` are valid
            ans += j - i + 1
            
        return ans