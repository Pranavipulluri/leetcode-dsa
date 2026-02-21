# Last updated: 6/2/2026, 12:00:50 PM
class Solution(object):
    def countMonobit(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=1
        x=1
        while x<=n:
            ans+=1
            x=(x<<1)|1
        return ans