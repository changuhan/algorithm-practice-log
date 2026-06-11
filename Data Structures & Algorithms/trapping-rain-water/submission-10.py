class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        for i in range(1, len(height) - 1):

            left = height[i]
            
            for j in range(i):
                left = max(left, height[j])


            right = height[i]
            for j in range(i + 1, len(height)):
                right = max(right, height[j])

            res += (min(left, right) - height[i])

        return res