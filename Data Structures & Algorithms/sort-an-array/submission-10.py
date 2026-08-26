class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        length = len(nums)

        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] >= nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        
        return nums

