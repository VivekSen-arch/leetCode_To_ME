class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        odd = 0
        middle = ""

        for i in range(26):
            if cnt[i] % 2 == 1:
                odd += 1
                middle = chr(ord('a') + i)

        if odd > 1:
            return ""

        half = [0] * 26

        for i in range(26):
            half[i] = cnt[i] // 2

        m = n // 2

        def make_pal(left):
            left = ''.join(left)

            if n % 2 == 1:
                return left + middle + left[::-1]

            return left + left[::-1]

        used = [0] * 26
        possible = True

        for i in range(m):
            c = ord(target[i]) - ord('a')
            used[c] += 1

            if used[c] > half[c]:
                possible = False
                break

        if possible:
            candidate = make_pal(list(target[:m]))

            if candidate > target:
                return candidate

        for pos in range(m - 1, -1, -1):

            used = [0] * 26
            possible = True

            for j in range(pos):
                c = ord(target[j]) - ord('a')
                used[c] += 1

                if used[c] > half[c]:
                    possible = False
                    break

            if not possible:
                continue

            cur = ord(target[pos]) - ord('a')

            for c in range(cur + 1, 26):

                if used[c] >= half[c]:
                    continue

                left = list(target[:pos])
                left.append(chr(ord('a') + c))

                rem = half[:]

                for x in range(26):
                    rem[x] -= used[x]

                rem[c] -= 1

                for x in range(26):
                    left.extend(
                        [chr(ord('a') + x)] * rem[x]
                    )

                return make_pal(left)

        return ""