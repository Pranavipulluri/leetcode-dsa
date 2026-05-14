# Last updated: 6/2/2026, 12:05:27 PM
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left,right=0,len(height)-1
        max_area=0
        while left<right:
            a=min(height[left],height[right])
            area=a*(right-left)
            max_area=max(area,max_area)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return max_area

        