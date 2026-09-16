class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        s_nums = sorted(nums)

        output = []
    
        for i in range(len(s_nums)-3):
            if i > 0 and s_nums[i] == s_nums[i-1]:
                continue
            for j in range(i+1, len(s_nums)-2):
                if j > i+1 and s_nums[j] == s_nums[j-1]:
                    continue
                
                left = j + 1
                right = len(nums) - 1

                while left < right: 
                    current_sum = s_nums[i] + s_nums[j] + s_nums[left] + s_nums[right]
                    if current_sum == target:
                        output.append([s_nums[i], s_nums[j], s_nums[left], s_nums[right]])
                        left += 1
                        right -= 1

                        while left < right and s_nums[left] == s_nums[left-1]:
                            left += 1

                        while left < right and s_nums[right] == s_nums[right+1]:
                            right -= 1

                    elif current_sum > target: 
                        right -= 1

                    else:
                        left += 1

        return output

                

