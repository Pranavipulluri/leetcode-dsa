# Last updated: 6/2/2026, 12:00:51 PM
class Solution(object):
    def nthSmallest(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        M=50
        c=[[0]*(M+1) for _ in range(M+1)]
        for i in range(M+1):
            c[i][0]=1
            for j in range(1,i+1):
                c[i][j]=c[i-1][j-1]+c[i-1][j]
        ans=0
        r=k
        for bit in range(M-1,-1,-1):
            if r==0:
                break
            if bit>=r:
                count=c[bit][r]
            else:
                count=0
            if count<n:
                n-=count
                ans|=(1<<bit)
                r-=1
        return ans