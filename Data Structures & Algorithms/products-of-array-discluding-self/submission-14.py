class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]
        left = 1
        right = 1

        for i in range(1, len(nums)):
            left = left * nums[i-1]
            output.append(left)

        for j in range(len(nums) - 1, -1, -1):
            output[j] = right * output[j]
            right = right * nums[j]

        return output