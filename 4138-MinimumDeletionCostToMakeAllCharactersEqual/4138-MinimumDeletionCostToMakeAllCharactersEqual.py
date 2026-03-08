# Last updated: 6/2/2026, 12:01:14 PM
class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        dict={}
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]]+=cost[i]
            else:
                dict[s[i]]=cost[i]
        s=sum(cost)
        max_keep=max(dict.values())
        return s-max_keep