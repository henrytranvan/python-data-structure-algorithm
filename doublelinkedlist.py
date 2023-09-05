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
        self.head.pre = None
        self.length -= 1

    def insert(self, pos, val):
        new_node = Node(val)
        current_node = self.head
        while current_node != None and current_node.value != pos:
            current_node = current_node.next
        if current_node == self.tail:
            self.append(val)
        else:
            current_node.next.pre = new_node
            new_node.next = current_node.next
            new_node.pre = current_node
            current_node.next = new_node

        self.length += 1
    def pop_out(self):
        self.tail = self.tail.pre
        self.tail.next = None



my_dll = DoubleLinkedList(10)
my_dll.append(20)
my_dll.append(30)
my_dll.append(40)
my_dll.append(50)
my_dll.append(60)
my_dll.append(70)
my_dll.print_dll()
my_dll.print_revert_dll()
print("==========")
my_dll.insert(50, 55)
my_dll.print_dll()
my_dll.print_revert_dll()
print("==========")
my_dll.delete()
my_dll.print_dll()
my_dll.print_revert_dll()
print("==========")
my_dll.pop_out()
my_dll.print_dll()
my_dll.print_revert_dll()
