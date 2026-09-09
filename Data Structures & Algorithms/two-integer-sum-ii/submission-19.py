class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right: 
            if target == numbers[right] + numbers[left]:
                return [left+1, right+1]

            elif target < numbers[right] + numbers[left]:
                right -= 1
            
            elif target > numbers[right] + numbers[left]:
                left += 1
        
         
         
         
         
         
         
         
         
         # right, left set up 

         # while left < right 
         # if target = left + right 
            # return [left, right]
         # elif: 
            # target > left + right:
            # left += 1
         # elif 
            # target < left + right:
            # right -= 1

        

        
