class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()

        for k, v in enumerate(nums):
            if v in hash_map:
                return [hash_map[v], k]
            hash_map[target - v] = k
        
        return None