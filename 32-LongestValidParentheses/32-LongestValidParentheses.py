# Last updated: 6/2/2026, 12:04:56 PM
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[-1]
        max_len=0
        for i,char in enumerate(s):
            if char=='(':
                stack.append(i)
            if char==')':
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len=max(max_len,i-stack[-1])
        return max_len