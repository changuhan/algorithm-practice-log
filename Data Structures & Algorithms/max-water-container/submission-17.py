class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxium = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left 

            current_water = height * width 

            maxium = max(current_water, maxium)

            if heights[left] < heights[right]:
                left += 1

            else:
                right -= 1
        
        return maxium
