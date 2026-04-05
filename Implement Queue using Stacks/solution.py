class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    def push(self, x: int) -> None:
        node = ListNode(x)
        node.next = self.head
        self.head = node
        self.size += 1
    def pop(self) -> int:
        val = self.head.val
        self.head = self.head.next
        self.size -= 1
        return val
    def peek(self) -> int:
        return self.head.val
    def empty(self) -> bool:
        return self.head is None
    def size(self) -> int:
        return self.size
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
