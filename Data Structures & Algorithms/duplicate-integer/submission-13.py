class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # review July 20th 2026:
        if len(nums) != len(set(nums)):
            return True 
        else: return False