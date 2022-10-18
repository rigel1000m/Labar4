import random


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

    def print(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next
    def search(self):
        node = self.head
        count = 0
        while node is not None:
            if node.prev is not None and node.next is not None:
                if node.prev.value < 0 and node.next.value < 0:
                    count += 1
            node = node.next
        return "Кол-во элементов между отрицательными числами: " + str(count)

list = DoubleLinkedList()
for i in range(10):
    list.append(random.randint(-20,10))
print(list.search())
