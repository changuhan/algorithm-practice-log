class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        s_people = sorted(people, reverse=True)
        
        heavy = 0
        light = len(people) - 1

        output = 0

        while heavy < light: 
            if s_people[heavy] + s_people[light] < limit:
                output += 1
                heavy += 1
                light -= 1

            elif s_people[heavy] + s_people[light] > limit:
                output += 1
                heavy += 1
            
            elif s_people[heavy] + s_people[light] == limit:
                output += 1
                heavy += 1
                light -= 1

        if heavy == light:
            output += 1

        return output

