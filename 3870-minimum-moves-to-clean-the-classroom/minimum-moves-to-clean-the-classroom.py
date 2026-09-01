class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        litter = {}
        sr = sc = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    sr, sc = i, j
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = len(litter)

        k = len(litter)

        if k == 0:
            return 0

        full = (1 << k) - 1

        q = deque()
        q.append((sr, sc, 0, energy, 0))

        best = {}

        best[(sr, sc, 0)] = energy

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, mask, en, moves = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                if en == 0:
                    continue

                new_en = en - 1
                new_mask = mask

                if classroom[nr][nc] == 'L':
                    bit = litter[(nr, nc)]
                    new_mask |= (1 << bit)

                if classroom[nr][nc] == 'R':
                    new_en = energy

                new_moves = moves + 1

                if new_mask == full:
                    return new_moves

                state = (nr, nc, new_mask)

                if state in best and best[state] >= new_en:
                    continue

                best[state] = new_en

                q.append((nr, nc, new_mask, new_en, new_moves))

        return -1