class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        

        while left <= right: 
            # convert mid to row, col and get the value
            # compare with target, then move left or right
            mid = (left + right) // 2
            row = mid // n
            col = mid % n

            value = matrix[row][col]

            if value < target:
                left = mid + 1
            elif value > target:
                right = mid - 1
            else:
                return True 

        return False 