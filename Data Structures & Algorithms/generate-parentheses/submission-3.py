class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        open_counts = 0
        close_counts = 0
        path = ""

        def backtrack(path, open_counts, close_counts):
            if len(path) == 2 * n:
                result.append(path)
                return result 

            if open_counts < n:
                backtrack(path + "(", open_counts + 1, close_counts)

            if close_counts < open_counts:
                backtrack(path + ")", open_counts, close_counts + 1)

            
        backtrack("", 0, 0)
        
        return result

            