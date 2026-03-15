# Last updated: 6/2/2026, 12:01:27 PM
from collections import defaultdict
class Solution(object):
    def countStableSubarrays(self, capacity):
        """
        :type capacity: List[int]
        :rtype: int
        """
        n=len(capacity)
        prefix=0
        count=0
        seen=defaultdict(int)
        for i,val in enumerate(capacity):
            
            if i-2>=0:
                l=i-2
                pp=prefix-capacity[i-1]
                seen[(capacity[l],pp)]+=1
            kf=(val,prefix-val)
            count+=seen[kf]
            prefix+=val
        return count
        