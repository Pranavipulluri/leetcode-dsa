# Last updated: 6/2/2026, 12:04:08 PM
import re
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pattern=r'^[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?$'
        result=re.match(pattern + r'\Z', s)
        if result:
            return True
        else:
            return False
        