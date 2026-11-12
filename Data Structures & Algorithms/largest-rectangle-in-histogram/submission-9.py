class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                area = height * (i - idx)
                max_area = max(max_area, area)

                start = idx # why do we have to change start to idx? 

            stack.append((start, h)) # if I replace start to i would it be stil working?


        for idx, height in stack:
            
            max_area = max(max_area, height * (len(heights) - idx))

        return max_area