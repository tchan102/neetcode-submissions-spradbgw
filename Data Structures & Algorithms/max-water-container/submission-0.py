class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0 
        R = len(heights) - 1
        global_max = 0
        while L < R:
            width = R - L
            height = min(heights[R], heights[L]) 
            global_max = max(int(width * height), global_max)
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1

        return global_max