class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # input: an int nums (list to search), int (the target sum)
        # output: a list with two int -> locations of the numbers that can sum up and equal to the taregt
        # the idea of this, is using memory again, this time with hash map, using the number has seen to be the index, and their index to be the value
        # so eachtime get the compliment of the current num and target, and see if the compliment is inside the memory map 

        complements = dict()

        for index, value in enumerate(nums):
            complement = target - value
            if complement in complements:
                return [complements[complement], index]
            complements[value] = index
        return None
