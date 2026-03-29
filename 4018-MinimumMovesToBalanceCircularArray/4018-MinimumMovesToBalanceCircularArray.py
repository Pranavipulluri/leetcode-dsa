# Last updated: 6/2/2026, 12:01:52 PM
class Solution(object):
    def minMoves(self, balance):
        """
        :type balance: List[int]
        :rtype: int
        """
        if sum(balance)<0:
            return -1
        n=len(balance)
        neg=-1
        for i in range(n):
            if balance[i]<0:
                neg=i
                break
        if neg==-1:
            return 0
        moves=0
        need=-balance[neg]
        d=1
        while need>0:
            l=(neg-d)%n
            r=(neg+d)%n
            if balance[l]>0:
                hoho=min(balance[l],need)
                balance[l]-=hoho
                need-=hoho
                moves +=hoho*d
            if need == 0:
                break
            if balance[r]>0:
                hehe=min(balance[r],need)
                balance[r]-=hehe
                need-=hehe
                moves +=hehe*d
            d+=1
        return moves