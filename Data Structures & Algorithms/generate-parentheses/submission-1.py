class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        open_count = 0
        close_count = 0
        path = ""


        def backtrack(path, open_count, close_count):
            if len(path) == 2 * n:
                result.append(path)
                return result
            
            if open_count < n:
                backtrack(path + "(", open_count + 1, close_count)

            if close_count < open_count:
                backtrack(path + ")", open_count, close_count + 1)


        
        
        backtrack("", 0, 0)

        return result