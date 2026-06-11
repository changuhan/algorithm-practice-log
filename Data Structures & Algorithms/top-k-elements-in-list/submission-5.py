class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        
        heap = []

        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for count, num in heap]
