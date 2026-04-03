# Last updated: 6/2/2026, 12:02:07 PM
class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        count=0
        island_groups = self.islands(grid)
        for i, group in enumerate(island_groups, 1):
            s=sum(group)
            if s%k==0:
                count+=1
        return count
    def islands(self, grid):
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        groups = []
    
        def dfs(r, c, group):
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                visited[r][c] or grid[r][c] == 0):
                return
            visited[r][c] = True
            group.append(grid[r][c])
            dfs(r + 1, c, group)
            dfs(r - 1, c, group)
            dfs(r, c + 1, group)
            dfs(r, c - 1, group)
    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0 and not visited[r][c]:
                    group = []
                    dfs(r, c, group)
                    if group:
                        groups.append(group)
    
        return groups
    
