class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums) 
        if not nums: return 0
        longest = 1

        for n in s:
            if n - 1 not in s:
                length = 1
                cur = n
                while cur + 1 in s:
                    cur += 1
                    length += 1
                longest = max(length, longest)
        return longest