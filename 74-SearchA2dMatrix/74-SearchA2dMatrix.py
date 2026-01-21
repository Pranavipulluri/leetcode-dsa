# Last updated: 6/2/2026, 12:03:53 PM
class Solution(object):
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])

        # --- Binary search on rows ---
        top = 0
        bottom = m - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            # If target is inside this row's range
            if matrix[mid][0] <= target <= matrix[mid][n - 1]:
                row = mid
                break
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                top = mid + 1
        else:
            return False  # no valid row found

        # --- Binary search inside that row ---
        left = 0
        right = n - 1
        
        while left <= right:
            mid = (left + right) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
