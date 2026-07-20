class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        for key in hash_map:
            if hash_map[key] == 1:
                return key
        return -1