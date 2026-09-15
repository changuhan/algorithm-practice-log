class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        s_nums = sorted(nums)
        
        output = []

        for i in range(len(s_nums) - 1):
            left = i + 1
            right = len(s_nums) - 1
            
            if i > 0 and s_nums[i] == s_nums[i-1]:
                continue

            while left < right: 
                current_sum = s_nums[i] + s_nums[left] + s_nums[right]
                
                if current_sum == 0:
                    output.append([s_nums[i], s_nums[left], s_nums[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and s_nums[left] == s_nums[left-1]:
                        left += 1
                    
                    while left < right and s_nums[right] == s_nums[right+1]:
                        right -= 1

                elif current_sum < 0:
                    left += 1
                
                elif current_sum > 0:
                    right -= 1
                
        return output