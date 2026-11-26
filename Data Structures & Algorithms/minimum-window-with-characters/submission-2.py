class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        need = {}
        window = {}

        for char in t:
            need[char] = need.get(char, 0) + 1

        left = 0
        have = 0
        required = len(need)

        min_length = float("inf")
        result = [-1, -1]

        for right, char in enumerate(s):

            # expand
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1

            # current window is valid
            while have == required:

                window_length = right - left + 1

                # save best answer
                if window_length < min_length:
                    min_length = window_length
                    result = [left, right]

                # shrink from left
                left_char = s[left]
                window[left_char] -= 1

                # did we break a requirement?
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        if min_length == float("inf"):
            return ""

        l, r = result
        return s[l:r + 1]