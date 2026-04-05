class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def push(self, x: int) -> None:
        node = ListNode(x)
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
        self.size += 1
    def pop(self) -> int:
        val = self.head.val
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return val
    def peek(self) -> int:
        return self.head.val
    def empty(self) -> bool:
        return self.head is None
    def size(self) -> int:
        return self.size
class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
    def push(self, x: int) -> None:
        self.q2.push(x)
        while not self.q1.empty():
            self.q2.push(self.q1.pop())
        self.q1, self.q2 = self.q2, self.q1
    def pop(self) -> int:
        return self.q1.pop()
    def top(self) -> int:
        return self.q1.peek()
    def empty(self) -> bool:
        return self.q1.empty()
