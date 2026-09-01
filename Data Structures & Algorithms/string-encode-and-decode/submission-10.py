class Solution:
# quick review 
    def encode(self, strs: List[str]) -> str:
        new_strs = [
            (str(len(word)) + "#" + word)
            for word in strs
        ]
        return "".join(new_strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):

            j = i

            while s[j] != "#":
                j += 1
                
            length = int(s[i:j]) # in case of 2 or more digits

            word = s[j + 1 : j + length + 1]

            result.append(word)

            i = j + length + 1

        return result 