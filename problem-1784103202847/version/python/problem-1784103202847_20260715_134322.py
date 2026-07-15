# Last updated: 7/15/2026, 1:43:22 PM
1class Solution(object):
2    def decodeString(self, s):
3        """
4        :type s: str
5        :rtype: str
6        """
7        currnum = ""
8        instack=[]
9        strstack=[]
10        realstr=""
11        for ch in s:
12            if ch.isdigit():
13                currnum += ch
14            elif ch == '[':
15                instack.append(int(currnum))
16                currnum = ""
17                strstack.append(ch)
18            elif ch==']':
19                curstr=""
20                while strstack[-1]!='[':
21                    curstr = strstack.pop() + curstr
22                strstack.pop()
23                num=instack.pop()
24                strstack.append(curstr * num)
25            else:
26                strstack.append(ch)
27        return "".join(strstack)
28