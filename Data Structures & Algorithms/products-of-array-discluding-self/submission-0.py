class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        left = 1

        for i in range(len(nums)):
            output.append(left)
            left = left * nums[i]

        right = 1

        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i] * right
            right = right * nums[i]

        return output