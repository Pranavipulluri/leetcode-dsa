# Last updated: 6/2/2026, 12:03:55 PM
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        ilist=[]
        jlist=[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    ilist.append(i)
                    jlist.append(j)
        for i in range(m):
            for j in range(n):
                if i in ilist or j in jlist:
                    matrix[i][j]=0
        return matrix