# Last updated: 6/2/2026, 12:02:59 PM
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n=len(prices)
        min_price=prices[0]
        dp=[0]*(n)
        for i in range(1,len(prices)):
            min_price=min(min_price,prices[i])
            dp[i]=max(dp[i-1],prices[i]-min_price)
        return dp[-1]