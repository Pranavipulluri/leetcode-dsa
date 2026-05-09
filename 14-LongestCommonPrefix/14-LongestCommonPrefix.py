# Last updated: 6/2/2026, 12:05:22 PM
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s=min(strs)
        ans=""
        for i in range(len(s)):
            a=s[i]
            for j in range(len(strs)):
                if a!=strs[j][i]:
                    return ans
            ans+=a
        return s
