# Last updated: 6/2/2026, 12:02:44 PM
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dp=[0]*(n+1)
        for i in range(1,n+1):
            dp[i]=dp[i>>1]+(i&1)
        return dp