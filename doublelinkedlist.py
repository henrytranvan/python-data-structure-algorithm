class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.pre = None


class DoubleLinkedList:
    def __init__(self, val):
        new_node = Node(val)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_dll(self):
        current_node = self.head
        while current_node != None:
            print(current_node.value)
            current_node = current_node.next

    def print_revert_dll(self):
        current_node = self.tail
        while current_node != None:
            print(current_node.value)
            current_node = current_node.pre

    def append(self, val):
        new_node = Node(val)
        new_node.pre = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def delete(self):
        self.head = self.head.next
        self.length -= 1

my_dll = DoubleLinkedList(10)
my_dll.append(20)
my_dll.append(30)
my_dll.print_dll()
my_dll.print_revert_dll()