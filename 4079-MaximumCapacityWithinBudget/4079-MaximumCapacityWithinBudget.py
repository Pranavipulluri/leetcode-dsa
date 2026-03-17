# Last updated: 6/2/2026, 12:01:32 PM
import bisect
class Solution(object):
    def maxCapacity(self, costs, capacity, budget):
        """
        :type costs: List[int]
        :type capacity: List[int]
        :type budget: int
        :rtype: int
        """
        machines=sorted(zip(costs,capacity))
        n=len(costs)
        pmax=[0]*n
        pmax[0]=machines[0][1]
        for i in range(1,n):
            pmax[i]=max(pmax[i-1],machines[i][1])
        ans=0
        for c,cap in machines:
            if c<budget:
                ans=max(ans,cap)
        costs_only=[c for c,_ in machines]
        for i in range(n):
            c,cap=machines[i]
            remain=budget-c
            if remain<=0:
                continue
            j=bisect.bisect_left(costs_only,remain,0,i)-1
            if j>=0:
                ans=max(ans,cap+pmax[j])
        
        
        return ans