class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = ""
        s = 0
        for digit in str(n):
            if digit != '0':
                x += digit
                s += int(digit)
        if x == "":
            return 0
        return int(x) * s
