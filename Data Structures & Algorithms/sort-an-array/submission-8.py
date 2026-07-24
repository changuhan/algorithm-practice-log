class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # bubble sort

        n = len(nums)

        for p in range(n - 1):
            swapped = False 
            for i in range(n - 1 - p):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swapped = True 

            if not swapped:
                break
        
        return nums