# Last updated: 6/2/2026, 12:03:39 PM
class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []  # will store indices
        max_area = 0
        
        # Add a zero height at end to flush out remaining bars
        heights.append(0)
        
        for i, h in enumerate(heights):
            # While current bar is smaller than stack top → calculate area
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                
                # width depends on whether stack is empty
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                
                max_area = max(max_area, height * width)
            
            stack.append(i)
        
        return max_area
