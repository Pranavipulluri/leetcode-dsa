# Last updated: 6/2/2026, 12:01:38 PM
import heapq
class AuctionSystem(object):

    def __init__(self):
        self.bids={}
        self.heap={}

    def addBid(self, userId, itemId, bidAmount):
        """
        :type userId: int
        :type itemId: int
        :type bidAmount: int
        :rtype: None
        """
        if itemId not in self.bids:
            self.bids[itemId]={}
            self.heap[itemId]=[]
        self.bids[itemId][userId]=bidAmount
        heapq.heappush(self.heap[itemId],(-bidAmount,-userId))
        

    def updateBid(self, userId, itemId, newAmount):
        """
        :type userId: int
        :type itemId: int
        :type newAmount: int
        :rtype: None
        """
        self.bids[itemId][userId]=newAmount
        heapq.heappush(self.heap[itemId],(-newAmount,-userId))

    def removeBid(self, userId, itemId):
        """
        :type userId: int
        :type itemId: int
        :rtype: None
        """
        del self.bids[itemId][userId]
        if not self.bids[itemId]:
            del self.bids[itemId]
            del self.heap[itemId]

    def getHighestBidder(self, itemId):
        """
        :type itemId: int
        :rtype: int
        """
        if itemId not in self.bids:
            return -1
        h=self.heap[itemId]
        bid=self.bids[itemId]
        while h:
            b,user=h[0]
            b=-b
            user=-user
            if user in bid and bid[user]==b:
                return user
            heapq.heappop(h)
        
        return -1


# Your AuctionSystem object will be instantiated and called as such:
# obj = AuctionSystem()
# obj.addBid(userId,itemId,bidAmount)
# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)