class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # input: array of int, integer occurance from 1 to len(nums), integer k -> the max k occrrence integer from nums 
        # output: a list of max k integer of most occurence integer

        count = {} # n from nums -> count
        res = []
        for n in nums:
            count[n] = count.get(n, 0) + 1
        count = dict(sorted(count.items(),key=lambda item: item[1], reverse=True))
        i = 0
        print(count)
        for key, val in count.items():
            if k == len(res): break
            res.append(key)


        return res