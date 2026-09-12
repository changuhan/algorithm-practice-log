class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        s_p = sorted(people, reverse=True)
        left = 0
        right = len(s_p) - 1
        output = 0
        while left < right:
            if s_p[left] + s_p[right] > limit:
                output += 1
                
                left += 1
            
            elif s_p[left] + s_p[right] == limit:
                output += 1

                left += 1
                right -= 1

            elif s_p[left] + s_p[right] < limit:
                output += 1

                left += 1
                right -= 1

        if left == right: 
            output += 1

        return output
                