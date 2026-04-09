class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = dict()
        for k, v in enumerate(nums):
            diff = target - v
            if v in hashMap:
                return [hashMap[v], k]
            hashMap[diff] = k
        return []