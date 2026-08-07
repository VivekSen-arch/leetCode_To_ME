from functools import lru_cache

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        temp = t
        req_a = req_b = req_c = req_d = 0
        while temp % 2 == 0: req_a += 1; temp //= 2
        while temp % 3 == 0: req_b += 1; temp //= 3
        while temp % 5 == 0: req_c += 1; temp //= 5
        while temp % 7 == 0: req_d += 1; temp //= 7
        
        if temp > 1:
            return "-1"

        @lru_cache(None)
        def min_len_23(a, b):
            a, b = max(0, a), max(0, b)
            if a == 0 and b == 0: 
                return 0
            
            res = float('inf')
            
            if a > 0:
                res = min(res, 1 + min_len_23(a - 3, b))     # Using '8'
                res = min(res, 1 + min_len_23(a - 2, b))     # Using '4'
                res = min(res, 1 + min_len_23(a - 1, b))     # Using '2'
            if b > 0:
                res = min(res, 1 + min_len_23(a, b - 2))     # Using '9'
                res = min(res, 1 + min_len_23(a, b - 1))     # Using '3'
            if a > 0 or b > 0:
                res = min(res, 1 + min_len_23(a - 1, b - 1)) # Using '6'
                
            return res

        def get_min_digits(req):
            return req[2] + req[3] + min_len_23(req[0], req[1])

        DIGIT_FACTORS = {
            1: (0, 0, 0, 0), 2: (1, 0, 0, 0), 3: (0, 1, 0, 0),
            4: (2, 0, 0, 0), 5: (0, 0, 1, 0), 6: (1, 1, 0, 0),
            7: (0, 0, 0, 1), 8: (3, 0, 0, 0), 9: (0, 2, 0, 0)
        }

        def subtract(req, digit):
            f = DIGIT_FACTORS[digit]
            return (
                max(0, req[0] - f[0]), 
                max(0, req[1] - f[1]), 
                max(0, req[2] - f[2]), 
                max(0, req[3] - f[3])
            )

        if '0' not in num:
            curr_req = (req_a, req_b, req_c, req_d)
            for char in num:
                curr_req = subtract(curr_req, int(char))
            if curr_req == (0, 0, 0, 0):
                return num

        N = len(num)
        
        prefix_reqs = [(req_a, req_b, req_c, req_d)]
        z = 0
        while z < N and num[z] != '0':
            prefix_reqs.append(subtract(prefix_reqs[-1], int(num[z])))
            z += 1
            
        for i in range(min(N - 1, z), -1, -1):
            curr_req = prefix_reqs[i]
            start_d = int(num[i]) + 1
            
            for d in range(start_d, 10):
                next_req = subtract(curr_req, d)
                
                if get_min_digits(next_req) <= N - 1 - i:
                    ans = [num[:i], str(d)]
                    curr_req = next_req
                    rem_len = N - 1 - i
                    
                    suffix = []
                    for _ in range(rem_len):
                        for next_d in range(1, 10):
                            cand_req = subtract(curr_req, next_d)
                            if get_min_digits(cand_req) <= rem_len - 1:
                                suffix.append(str(next_d))
                                curr_req = cand_req
                                rem_len -= 1
                                break
                                
                    ans.append("".join(suffix))
                    return "".join(ans)
                    
        req = (req_a, req_b, req_c, req_d)
        req_len = max(N + 1, get_min_digits(req))
        ans = []
        
        for _ in range(req_len):
            for d in range(1, 10):
                cand_req = subtract(req, d)
                if get_min_digits(cand_req) <= req_len - 1:
                    ans.append(str(d))
                    req = cand_req
                    req_len -= 1
                    break
                    
        return "".join(ans)