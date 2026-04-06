class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
class LinkedStack:
    def __init__(self, freq=0):
        self.freq = freq
        self.head = None
        self.next = None
    def push(self, x: int) -> None:
        node = ListNode(x)
        node.next = self.head
        self.head = node
    def pop(self) -> int:
        val = self.head.val
        self.head = self.head.next
        return val
    def empty(self) -> bool:
        return self.head is None
class FreqNode:
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq
        self.next = None
class FreqStack:
    def __init__(self):
        self.freq_head = None   # linked list: val → freq
        self.group_head = None  # linked list: freq → LinkedStack
        self.max_freq = 0
    def get_freq(self, val: int) -> int:
        node = self.freq_head
        while node:
            if node.val == val:
                return node.freq
            node = node.next
        return 0
    def set_freq(self, val: int, freq: int) -> None:
        node = self.freq_head
        while node:
            if node.val == val:
                node.freq = freq
                return
            node = node.next
        new_node = FreqNode(val, freq)
        new_node.next = self.freq_head
        self.freq_head = new_node
    def get_or_create_stack(self, freq: int) -> LinkedStack:
        node = self.group_head
        while node:
            if node.freq == freq:
                return node
            node = node.next
        new_stack = LinkedStack(freq)
        new_stack.next = self.group_head
        self.group_head = new_stack
        return new_stack
    def push(self, val: int) -> None:
        f = self.get_freq(val) + 1
        self.set_freq(val, f)
        if f > self.max_freq:
            self.max_freq = f
        self.get_or_create_stack(f).push(val)
    def pop(self) -> int:
        stack = self.get_or_create_stack(self.max_freq)
        val = stack.pop()
        self.set_freq(val, self.get_freq(val) - 1)
        if stack.empty():
            self.max_freq -= 1
        return val
