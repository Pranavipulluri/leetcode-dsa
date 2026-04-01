# Last updated: 6/2/2026, 12:02:03 PM
class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        sorted_nums=sorted(nums)
        if nums==sorted_nums:
            return 0
        val_to_idx = {v: i for i, v in enumerate(nums)}
        def sorts(k):
            parent=list(range(n))
            def find(b):
                while parent[b]!=b:
                    parent[b]=parent[parent[b]]
                    b=parent[b]
                return b
            def union(x,y):
                px,py=find(x),find(y)
                if px!=py:
                    parent[px]=py
            group = [i for i, v in enumerate(nums) if (v & k) == k]
            for i in range(1, len(group)):
                union(group[0], group[i])
            for i in range(n):
                #target_val=sorted_nums[i]
                target_idx = val_to_idx[sorted_nums[i]]
                if find(i)!=find(target_idx):
                    return False
            return True
        k=0
        for bit in reversed(range(max(nums).bit_length() + 1)):
            test_k=k| (1<<bit)
            if sorts(test_k):
                k=test_k
        return k
        