# Last updated: 6/2/2026, 12:05:14 PM
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        braces = []
        for ch in s:
            if ch in {'(', '[', '{'}:
                braces.append(ch)
            elif ch == ')':
                if not braces or braces[-1] != '(':
                    return False
                braces.pop()
            elif ch == ']':
                if not braces or braces[-1] != '[':
                    return False
                braces.pop()
            elif ch == '}':
                if not braces or braces[-1] != '{':
                    return False
                braces.pop()
            else:
                # For any invalid character
                return False
        
        return len(braces) == 0