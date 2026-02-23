# Last updated: 6/2/2026, 12:00:55 PM
from collections import deque
class Solution(object):
    def specialNodes(self, n, edges, x, y, z):
        """
        :type n: int
        :type edges: List[List[int]]
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def bfs(start):
            d=[-1]*n
            d[start]=0
            q=deque([start])
            while q:
                node=q.popleft()
                for nei in adj[node]:
                    if d[nei]==-1:
                        d[nei]=d[node]+1
                        q.append(nei)
            return d
        dx=bfs(x)
        dy=bfs(y)
        dz=bfs(z)
        def pyth(a,b,c):
            a,b,c=sorted([a,b,c])
            return a*a+b*b==c*c
        c=0
        for i in range(n):
            if pyth(dx[i],dy[i],dz[i]):
                c+=1
        return c