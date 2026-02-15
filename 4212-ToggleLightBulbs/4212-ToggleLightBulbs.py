# Last updated: 6/2/2026, 12:00:35 PM
class Solution(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """
        freq={}
        for i in range(len(bulbs)):
            if bulbs[i] in freq:
                freq[bulbs[i]]+=1
            else:
                freq[bulbs[i]]=1
        on=[]
        for key,val in freq.items():
            if val%2!=0:
                on.append(key)
        on.sort()
        return on