# Last updated: 6/2/2026, 12:02:29 PM
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        m=len(grid[0])
        fresh=[]
        rotten=[]
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    fresh.append((i,j))
                elif grid[i][j]==2:
                    rotten.append((i,j))
        change=1
        minutes=0
        while change:
            newrotten=[]
            change=0
            for (a,b) in rotten:
                if (a+1,b) in fresh:
                    fresh.remove((a+1,b))
                    newrotten.append((a+1,b))
                    change=1
                if (a-1,b) in fresh:
                    fresh.remove((a-1,b))
                    newrotten.append((a-1,b))
                    change=1
                if (a,b+1) in fresh:
                    fresh.remove((a,b+1))
                    newrotten.append((a,b+1))
                    change=1
                if (a,b-1) in fresh:
                    fresh.remove((a,b-1))
                    newrotten.append((a,b-1))
                    change=1
            if change:
                minutes+=1
                rotten+=newrotten
        if fresh:
            return -1
        else:
            return minutes