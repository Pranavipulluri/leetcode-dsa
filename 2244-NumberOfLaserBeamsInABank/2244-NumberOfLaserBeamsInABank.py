# Last updated: 6/2/2026, 12:02:19 PM
class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        prev=0
        res=0
        for row in bank:
            s=0
            for i in range(len(row)):
                s+=int(row[i])
            print(s)
            print(prev)
            if row>0 and s!=0:
                res+=prev*s
                prev=s
                print("hello {}".format(res))
        return res