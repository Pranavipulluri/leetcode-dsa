# Last updated: 6/2/2026, 12:03:44 PM
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=1
        freq=1
        cn=nums[0]
        for j in range(1,len(nums)):
            if nums[j]==cn:
                if freq<2:
                    freq+=1
                    nums[i]=nums[j]
                    i+=1
                else:
                    continue
            else:
                cn=nums[j]
                freq=1
                nums[i]=nums[j]
                i+=1
        return i
        