# Last updated: 6/2/2026, 12:01:19 PM
class RideSharingSystem(object):

    def __init__(self):
        self.riders=deque()
        self.drivers=deque()
        self.cancelled=set()

    def addRider(self, riderId):
        """
        :type riderId: int
        :rtype: None
        """
        self.riders.append(riderId)
        self.cancelled.add(riderId)

    def addDriver(self, driverId):
        """
        :type driverId: int
        :rtype: None
        """
        self.drivers.append(driverId)

    def matchDriverWithRider(self):
        """
        :rtype: List[int]
        """
        if not self.drivers or not self.riders:
            return [-1,-1]
        driver=self.drivers.popleft()
        rider=self.riders.popleft()
        self.cancelled.remove(rider)
        return [driver,rider]

    def cancelRider(self, riderId):
        """
        :type riderId: int
        :rtype: None
        """
        if riderId in self.cancelled:
            self.cancelled.remove(riderId)
            self.riders=deque(i for i in self.riders if i!=riderId)


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)