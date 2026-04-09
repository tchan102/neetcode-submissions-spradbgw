class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # set => all item unique
        # if len(set) == len(arr) = no duplicate
        return len(set(nums)) != len(nums) 