class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def solve(s):
            result = {""}
            current = {""}
            union = set()

            i = 0

            while i < len(s):

                if s[i] == '{':
                    count = 1
                    j = i + 1

                    while count:
                        if s[j] == '{':
                            count += 1
                        elif s[j] == '}':
                            count -= 1
                        j += 1

                    inside = s[i + 1:j - 1]
                    current = multiply(current, solve(inside))
                    i = j

                elif s[i] == ',':
                    union |= current
                    current = {""}
                    i += 1

                else:
                    current = multiply(current, {s[i]})
                    i += 1

            union |= current
            return union

        def multiply(a, b):
            result = set()

            for x in a:
                for y in b:
                    result.add(x + y)

            return result

        return sorted(solve(expression))