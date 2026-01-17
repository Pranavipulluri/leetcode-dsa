# Last updated: 6/2/2026, 12:03:37 PM
class Solution(object):

    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        
        temp = heights + [0]  # safe flush
        
        for i, h in enumerate(temp):
            while stack and temp[stack[-1]] > h:
                height = temp[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        return max_area

    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        heights = [0] * cols
        max_area = 0
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0
            
            max_area = max(max_area,
                           self.largestRectangleArea(heights))
        
        return max_area
