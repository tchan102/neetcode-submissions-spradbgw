class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) - 1
        global_volume = 0
        while l < r: 
            width = r - l
            height = min(heights[l], heights[r])
            global_volume = max(width * height, global_volume)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return global_volume
            