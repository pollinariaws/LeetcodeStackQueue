from collections import deque
class Queue:
    def __init__(self):
        self.data = deque()
    def push(self, x):
        self.data.append(x)
    def pop(self):
        return self.data.popleft()
    def peek(self):
        return self.data[0]
    def empty(self):
        return len(self.data) == 0
    def size(self):
        return len(self.data)
class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
    def push(self, x):
        self.q2.push(x)
        while not self.q1.empty():
            self.q2.push(self.q1.pop())
        self.q1, self.q2 = self.q2, self.q1
    def top(self):
        return self.q1.peek()
    def empty(self):
        return self.q1.empty()
    def pop(self):
        return self.q1.pop()
