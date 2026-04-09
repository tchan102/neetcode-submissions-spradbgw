class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums) 
        if not nums: return 0
        global_max = 1
        for k in s:
            if k - 1 in s:
                continue
            
            local_max = 1
            d = k
            while d + 1 in s:
                local_max += 1
                d += 1
            global_max = max(local_max, global_max) 
        
        return global_max
            
