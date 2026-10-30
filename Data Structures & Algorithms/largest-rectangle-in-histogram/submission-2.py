class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest = 0

        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > h:
                top = stack.pop()
                left = stack[-1] if stack else -1
                width = i - left - 1
                largest = max(largest, heights[top] * width)
            
            stack.append(i)

        return largest
                 


        
