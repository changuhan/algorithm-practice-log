class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        longest = 0 

        for right, char in enumerate(s):
            while char in seen:
                seen.remove(s[left])
                
                left += 1
            
            seen.add(char)

            window_length = right - left + 1
            
            longest = max(longest, window_length)

        return longest
