class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(x):
            count = 0
            
            for ch in x:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    
                    if count < 0:
                        return False
            
            return count == 0
        
        queue = {s}
        
        while queue:
            
            ans = []
            
            for x in queue:
                if isValid(x):
                    ans.append(x)
            
            if ans:
                return ans
            
            next_level = set()
            
            for x in queue:
                for i in range(len(x)):
                    if x[i] not in '()':
                        continue
                    
                    new_string = x[:i] + x[i + 1:]
                    next_level.add(new_string)
            
            queue = next_level
        
        return [""]