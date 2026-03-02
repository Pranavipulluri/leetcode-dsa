# Last updated: 6/2/2026, 12:01:06 PM
class Solution(object):
    def minimumOR(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        ans=0
        for bit in reversed(range(31)):
            cand=ans | ((1<<bit)-1)
            nana=True
            for rown in grid:
                found=False
                for num in rown:
                    if (num & ~(cand))==0:
                        found=True
                        break
                if not found:
                    nana=False
                    break
            if not nana:
                ans|=(1<<bit)
        return ans