class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """ 
        result > sort > for loop if second i same as first one > while l < r: define sum > conditional > if num[l] == num[r] move l 
        """

        res = [] # output 
        nums.sort() # sorted list

        for index, value in enumerate(nums):
            if index > 0 and nums[index] == nums[index-1]:
                continue

            l, r = index + 1, len(nums) - 1

            while l < r:
                s = value + nums[l] + nums[r]

                if s > 0:
                    r -= 1

                elif s < 0: 
                    l += 1

                else: 
                    res.append([value, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res