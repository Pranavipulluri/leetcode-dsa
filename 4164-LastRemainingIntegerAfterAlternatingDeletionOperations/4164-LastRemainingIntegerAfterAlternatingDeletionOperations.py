# Last updated: 6/2/2026, 12:01:03 PM
class Solution(object):
    def lastInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        left=True
        head=1
        step=1
        remaining=n
        while remaining>1:
            if not left and remaining%2==0:
                    head+=step
            step*=2
            remaining=(remaining+1)//2
            left=not left
        return head