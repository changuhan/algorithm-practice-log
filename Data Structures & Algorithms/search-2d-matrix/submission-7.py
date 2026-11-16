class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a, b = len(matrix[0]),len(matrix)
        low, high = 0, (a * b) - 1

        while low <= high:
            mid = (low + high) // 2
            row = mid // a
            col = mid % a

            value = matrix[row][col]

            if value < target: 
                low = mid + 1

            elif value > target: 
                high = mid - 1

            else:
                return True 

        return False
            

        