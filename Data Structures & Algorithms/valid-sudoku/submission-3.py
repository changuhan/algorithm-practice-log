class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        for row in board:
            seen = set()

            for value in row:
                if value == ".":
                    continue 
                elif value in seen:
                    return False 
                else: 
                    seen.add(value)
        
        for c in range(9):
            seen = set()

            for r in range(9):
                value = board[r][c]

                if value == ".":
                    continue
                elif value in seen:
                    return False
                else:
                    seen.add(value) 

        for start_r in range(0, 9, 3):
            for start_c in range(0, 9, 3):
                seen = set()

                for r in range(start_r, start_r + 3):
                    for c in range(start_c, start_c + 3):
                        value = board[r][c]
                    
                        if value == '.':
                            continue
                        elif value in seen:
                            return False
                        else:
                            seen.add(value)



        return True 
                