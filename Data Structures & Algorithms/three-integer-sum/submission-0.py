class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def helper(s, k):
            d = {}
            found = []
            for i, c in enumerate(s):
                complement = k - c
                if complement in d:
                    found.append([complement, c])
                d[c] = i
            return found
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            new_s = nums[i + 1:]
            results = helper(new_s, -1 * nums[i])
            for r in results:
                triplet = [nums[i], r[0], r[1]]
                if triplet not in res:
                    res.append(triplet)
        return res