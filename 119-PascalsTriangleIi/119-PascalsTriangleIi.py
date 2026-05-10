# Last updated: 6/2/2026, 12:03:01 PM
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        prev=[]
        numRows=rowIndex
        for i in range(1,numRows+2):
            if i==1:
                prev.append(1)
            else:
                curr=[]
                curr.append(1)
                if len(prev)>1:
                    for j in range(1,len(prev)):
                        curr.append(prev[j-1]+prev[j])
                curr.append(1)
                prev=curr
        return prev

        