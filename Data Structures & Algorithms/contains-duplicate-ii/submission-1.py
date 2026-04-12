class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {} 
        for index, value in enumerate(nums): 
            if value in seen and abs(seen[value] - index) <= k:
                return True
            seen[value] = index
        return False