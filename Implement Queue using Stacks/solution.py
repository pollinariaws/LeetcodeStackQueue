class Stack:
    def __init__(self):
        self.data = []
    def push(self, x: int) -> None:
        self.data.append(x)
    def pop(self) -> int:
        return self.data.pop()
    def peek(self) -> int:
        return self.data[-1]
    def empty(self) -> bool:
        return len(self.data) == 0
    def size(self):
        return len(self.data)
class MyQueue:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()
    def push(self, x: int) -> None:
        self.inbox.push(x)
    def transfer(self) -> None:
        if self.outbox.empty():
            while not self.inbox.empty():
                self.outbox.push(self.inbox.pop())
    def pop(self) -> int:
        self.transfer()
        return self.outbox.pop()
    def peek(self) -> int:
        self.transfer()
        return self.outbox.peek()
    def empty(self) -> bool:
        return self.inbox.empty() and self.outbox.empty()
