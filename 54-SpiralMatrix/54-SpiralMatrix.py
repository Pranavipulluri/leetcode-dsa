# Last updated: 6/2/2026, 12:04:24 PM
'''
pop top row of matrix. that's the your first part of your path

rotate matrix 90deg counterclockwise

recurse on the rest of the matrix to find rest of path
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        first_row = list(matrix.pop(0))  # deep copy
        if not matrix:
            return first_row

        # rotate 90deg counterclockwise by transposing then reversing
        rotated = list(zip(*matrix))[::-1]

        return first_row + self.spiralOrder(rotated)