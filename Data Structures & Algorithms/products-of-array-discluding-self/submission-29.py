class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        left = 1
        right = 1 

        for i in range(len(nums)):
            output.append(left)
            left = left * nums[i]

        for j in range(len(nums) - 1, -1 , -1):
            output[j] = output[j] * right 
            right = right * nums[j]

        return output