class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        conditions:
        1. we can't sort the list

        steps:
        two pointers:
        what about we compare every single amount of water trough interation? 
        contain every single value in the list and find the maxium value
        what about we update the maxium throughout the interation? 

        1. index between two values are going be the width
        2. 

        """

        best = 0 

        l, r = 0, len(heights) - 1

        while l < r:
            width = r - l 
            height = min(heights[l], heights[r])
            best = max(best, height * width)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return best

    
        