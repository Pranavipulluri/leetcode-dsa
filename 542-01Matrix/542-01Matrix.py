# Last updated: 6/2/2026, 12:02:41 PM
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        n=len(mat)
        m=len(mat[0])
        ans = [[-1 for _ in range(m)] for _ in range(n)]
        zeros=[]
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    zeros.append((i,j))
        for (a,b) in zeros:
            ans[a][b]=0
        val=1
        while any(-1 in row for row in ans):
            updated=[]
            for (a,b) in zeros:
                if a+1<n and ans[a+1][b]==-1:
                    ans[a+1][b]=val
                    updated.append((a+1,b))
                if b+1<m and ans[a][b+1]==-1:
                    ans[a][b+1]=val
                    updated.append((a,b+1))
                if  a-1>=0 and ans[a-1][b]==-1:
                    ans[a-1][b]=val
                    updated.append((a-1,b))
                if  b-1>=0 and ans[a][b-1]==-1:
                    ans[a][b-1]=val
                    updated.append((a,b-1))
            zeros=updated
            val+=1
        return ans
