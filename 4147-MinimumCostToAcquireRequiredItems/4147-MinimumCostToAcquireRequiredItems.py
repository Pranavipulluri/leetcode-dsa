# Last updated: 6/2/2026, 12:01:13 PM
class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """
        if costBoth<cost1+cost2:
            n=min(need1,need2)
            ans=(n*costBoth)
            need1-=n
            need2-=n
            if need1>0:
                if cost1>costBoth:
                    ans+=need1*costBoth
                else:
                    ans+=cost1*need1
            else:
                if cost2>costBoth:
                    ans+=need2*costBoth
                else:
                    ans+=cost2*need2
        else:
            ans=need1*cost1+need2*cost2
        return ans