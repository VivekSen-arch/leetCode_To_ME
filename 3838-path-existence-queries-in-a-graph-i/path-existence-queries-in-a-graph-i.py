class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        component = [0] * n
        for i in range(1, n):
            component[i] = component[i - 1]
            if nums[i] - nums[i - 1] > maxDiff:
                component[i] += 1
        answer = []
        for u, v in queries:
            answer.append(component[u] == component[v])
        return answer