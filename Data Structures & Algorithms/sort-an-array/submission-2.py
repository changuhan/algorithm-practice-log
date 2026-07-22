class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        # Traverse through all array elements
        for i in range(n):
            # Last i elements are already in place
            for j in range(0, n - i - 1):
                # Swap if the element found is greater than the next element
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums