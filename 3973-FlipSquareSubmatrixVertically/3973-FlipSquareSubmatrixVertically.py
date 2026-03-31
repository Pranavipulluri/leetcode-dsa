# Last updated: 6/2/2026, 12:01:57 PM
class Solution(object):
    def reverseSubmatrix(self, grid, x, y, k):
        """
        :type grid: List[List[int]]
        :type x: int
        :type y: int
        :type k: int
        :rtype: List[List[int]]
        """
        for i in range(k//2):
            tr=x+i
            br=x+(k-1-i)
            for col in range(y,y+k):
                grid[tr][col],grid[br][col]=grid[br][col],grid[tr][col]
        return grid
        
        
        