class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # review July 23, 2026 
        if len(set(nums)) != len(nums):
            return True
        return False 