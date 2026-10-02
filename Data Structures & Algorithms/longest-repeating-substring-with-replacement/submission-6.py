class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        left = 0
        longest = 0

        for right, char in enumerate(s):
            seen[char] = seen.get(char, 0) + 1
            window_length = right - left + 1
            need_k = window_length - max(seen.values())

            while need_k > k:
                seen[s[left]] -= 1
                left += 1
                window_length = right - left + 1
                need_k = window_length - max(seen.values())

            longest = max(longest, window_length)

        return longest