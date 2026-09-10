class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        s_list = sorted(nums)

        output = []
        
        for init in range(len(s_list)):
            if init > 0 and s_list[init] == s_list[init-1]:
                continue
                
            left = init + 1
            right = len(s_list) - 1

            while left < right:
                current_sum = s_list[init] + s_list[left] + s_list[right]
                if current_sum == 0:
                    output.append([s_list[init], s_list[left], s_list[right]])
                
                    left += 1
                    right -= 1
                
                    while left < right and s_list[left] == s_list[left - 1]:
                        left += 1

                    while left < right and s_list[right] == s_list[right + 1]:
                        right -= 1

                elif current_sum > 0:
                    right -= 1

                else: 
                    left += 1

        return output
                    

        