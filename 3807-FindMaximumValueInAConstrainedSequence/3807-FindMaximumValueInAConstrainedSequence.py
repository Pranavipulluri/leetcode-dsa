# Last updated: 6/2/2026, 12:02:08 PM
class Solution(object):
    def findMaxVal(self, n, restrictions, diff):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :type diff: List[int]
        :rtype: int
        """
        ub=[0]*n
        for i in range(1,n):
            ub[i]=ub[i-1]+diff[i-1]
        for i,j in restrictions:
            ub[i]=min(ub[i],j)
        for i in range(1,n):
            ub[i]=min(ub[i],ub[i-1]+diff[i-1])
        for i in range(n-2,-1,-1):
            ub[i]=min(ub[i],ub[i+1]+diff[i])
        return max(ub)