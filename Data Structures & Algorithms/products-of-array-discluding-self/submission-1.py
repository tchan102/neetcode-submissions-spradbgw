class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) 
        prefix = 1
        for _ in range(len(nums)):
            res[_] = prefix
            prefix *= nums[_]

        postfix = 1
        for _ in range(len(nums) - 1, - 1, -1):
            res[_] *= postfix
            postfix *= nums[_]
        return res
        