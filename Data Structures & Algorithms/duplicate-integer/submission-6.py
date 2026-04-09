class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # input: an array unsorted, with int 
        # output: bool => tell whether duplicate value in list or not
        # set => all item unique
        # if len(set) == len(arr) = no duplicate
        # return len(set(nums)) != len(nums) 

        # or approach as the same way, use O(1) search feature with set to find if duplicate exist while iterating the array 
        seen = set() 
        for _ in nums:
            if _ in seen:
                return True 
            seen.add(_)
        return False