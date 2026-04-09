class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0 
        R = len(nums) - 1

        if nums[L] <= nums[R]:
            return nums[0]

        while L <= R:
            mid = (R - L) // 2 + L 
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]

            if nums[mid] >= nums[0]:
                L = mid + 1
            else:
                R = mid - 1
        
        return nums[0]