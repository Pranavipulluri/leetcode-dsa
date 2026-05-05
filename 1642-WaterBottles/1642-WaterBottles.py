# Last updated: 6/2/2026, 12:02:23 PM
class Solution(object):
    def numWaterBottles(self, numbottles, numexchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        drink=numbottles
        emptybottles=numbottles
        while emptybottles>=numexchange:
            numbottles=emptybottles//numexchange
            emptybottles=emptybottles%numexchange
            drink+=numbottles
            emptybottles+=numbottles
        return drink
        

