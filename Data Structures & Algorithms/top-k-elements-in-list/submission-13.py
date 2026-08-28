class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap counts
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
         
        sorted_counts = sorted(
            counts.items(), 
            key=lambda item: item[1], 
            reverse=True)
        
        result = []

        for num, freq in sorted_counts[:k]:
            result.append(num)
        
        return result