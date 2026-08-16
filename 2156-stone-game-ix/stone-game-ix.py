class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0, 0, 0]
        for x in stones:
            cnt[x % 3] += 1
        zero = cnt[0]
        one = cnt[1]
        two = cnt[2]
        if one == 0 and two == 0:
            return False
        if zero % 2 == 0:
            return one > 0 and two > 0
        return abs(one - two) > 2