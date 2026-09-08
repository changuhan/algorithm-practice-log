class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}
        major = len(nums) // 3
        output = []
        
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for key, value in counts.items():
            if value > major:
                output.append(key)
        
        return output
