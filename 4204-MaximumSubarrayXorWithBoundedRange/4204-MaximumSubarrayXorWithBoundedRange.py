# Last updated: 6/2/2026, 12:00:44 PM

from collections import deque
class TrieNode:
    def __init__(self):
        self.child=[None,None]
        self.count=0
class Trie:
    def __init__(self):
        self.root=TrieNode()
        self.BITS=32
    def insert(self,num):
        node=self.root
        for i in reversed(range(self.BITS)):
            b=(num>>i)&1
            if not node.child[b]:
                node.child[b]=TrieNode()
            node=node.child[b]
            node.count+=1
    def remove(self,num):
        node=self.root
        for i in reversed(range(self.BITS)):
            b=(num>>i)&1
            nxt=node.child[b]
            nxt.count-=1
            node=nxt
    def max_xor(self,num):
        node=self.root
        ans=0
        for i in reversed(range(self.BITS)):
            b=(num>>i)&1
            want=1-b
            if node.child[want] and node.child[want].count>0:
                ans |=(1<<i)
                node=node.child[want]
            else:
                node=node.child[b]
        return ans
class Solution(object):
    def maxXor(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        prefix=[0]*(n+1)
        for i in range(n):
            prefix[i+1]=prefix[i]^nums[i]
        maxdq=deque()
        mindq=deque()
        trie=Trie()
        trie.insert(0)
        L=0
        ans=0
        for r in range(n):
            while maxdq and nums[maxdq[-1]]<=nums[r]:
                maxdq.pop()
            maxdq.append(r)
            while mindq and nums[mindq[-1]]>=nums[r]:
                mindq.pop()
            mindq.append(r)
            while nums[maxdq[0]]-nums[mindq[0]]>k:
                if maxdq[0]==L:
                    maxdq.popleft()
                if mindq[0]==L:
                    mindq.popleft()
                trie.remove(prefix[L])
                L+=1
            ans=max(ans,trie.max_xor(prefix[r+1]))
            trie.insert(prefix[r+1])
        return ans
        