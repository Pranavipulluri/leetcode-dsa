# Last updated: 6/2/2026, 12:01:04 PM
class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_dict={}
        for i in nums:
            if i in count_dict:
                count_dict[i]+=1
            else:
                count_dict[i]=1
        repeated={num:count for num,count in count_dict.items() if count>1}
        if len(repeated)==0:
            return 0
        j=0
        c=0
        while j<len(nums):
            for i in nums[j:j+3]:
                if i in repeated:
                    repeated[i]-=1
                    if repeated[i]==1:
                        del repeated[i]
            c+=1
            if len(repeated)==0:
                return c
            j+=3