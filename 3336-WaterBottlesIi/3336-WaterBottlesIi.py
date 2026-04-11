# Last updated: 6/2/2026, 12:02:14 PM
class Solution(object):
    def maxBottlesDrunk(self, numbottles, numexchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        emptybottles=numbottles
        drink=emptybottles
        while emptybottles>=numexchange:
            emptybottles-=numexchange
            numexchange+=1
            emptybottles+=1
            drink+=1
        return drink