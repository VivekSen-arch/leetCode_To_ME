
import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:

        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)

        busy = []
        ans = []

        time = 0
        j = 0
        m = len(tasks)

        while j < m:

            # Release all servers that have finished
            while busy and busy[0][0] <= time:
                end, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))

            # If no server is free, jump to next completion
            if not free:
                time = busy[0][0]
                continue

            # Assign all available queued tasks
            while free and j < m and j <= time:

                w, i = heapq.heappop(free)

                ans.append(i)

                heapq.heappush(
                    busy,
                    (time + tasks[j], w, i)
                )

                j += 1

            time += 1

        return ans
