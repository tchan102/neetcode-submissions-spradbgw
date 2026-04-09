class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums) 
        if not nums: return 0
        local_long = 1 
        global_long = 1

        for n in nums:
            if n - 1 not in s:
                cur = n
                while cur + 1 in s:
                    cur += 1
                    local_long += 1
                global_long = max(global_long, local_long)
                local_long = 1
        return max(global_long, local_long)