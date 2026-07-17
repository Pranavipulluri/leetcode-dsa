# Last updated: 7/17/2026, 8:19:50 AM
1class MyCircularQueue:
2
3    def __init__(self, k):
4        self.size = 0
5        self.max_size = k
6        self.t = [0]*k
7        self.front = self.rear = -1
8        
9    def enQueue(self, value):
10        if self.size == self.max_size: return False
11        else:
12            if self.rear == -1:
13                self.rear = self.front = 0
14            else:
15                self.rear = (self.rear + 1)%self.max_size
16            self.t[self.rear] = value
17            self.size += 1
18            return True
19        
20    def deQueue(self):
21        if self.size == 0: return False
22        if self.front == self.rear:
23            self.front = self.rear = -1
24        else:
25            self.front = (self.front + 1)%self.max_size
26        self.size -= 1
27        return True
28        
29
30    def Front(self):
31        return self.t[self.front] if self.size != 0 else -1
32
33    def Rear(self):
34        return self.t[self.rear] if self.size != 0 else -1
35
36    def isEmpty(self):
37        return self.size == 0
38
39    def isFull(self):
40        return self.size == self.max_size