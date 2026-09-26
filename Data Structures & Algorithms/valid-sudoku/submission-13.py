class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for r in range(9):
            seen = set()
            for c in range(9):
                
                val = board[r][c]
                if val == ".":
                    continue

                elif val in seen:
                    return False 
                
                else: 
                    seen.add(val)

        for c in range(9):
            seen = set()
            for r in range(9):
                
                val = board[r][c]
                
                if val == ".":
                    continue

                elif val in seen:
                    return False 
                
                else: 
                    seen.add(val)

        for start_r in range(0, 9, 3):
            for start_c in range(0, 9, 3):
                
                seen = set()

                for r in range(start_r, start_r + 3):
                    for c in range(start_c, start_c + 3):
                        

                        val = board[r][c]
                        if val == ".":
                            continue

                        elif val in seen:
                            return False 
                        
                        else: 
                            seen.add(val)

        return True