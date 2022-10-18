class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.size = 0

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def append(self,data):
        node = Node(data)
        self.size +=1
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.tail = node
            self.head = node
    def iterate(self):
        current_item = self.head
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    def getSize(self):
        return self.size
