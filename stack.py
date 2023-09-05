class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class Stack:
    def __init__(self, val):
        new_node = Node(val)
        self.top = new_node
        self.height = 1

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node

    def print(self):
        current_node = self.top
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    def pop(self):
        if self.top is not None:
            val = self.top.value
            if self.top.next is not None:
                self.top = self.top.next
            return val
        else:
            print("Stack is empty")
            return None


my_stack = Stack(20)
my_stack.push(30)
my_stack.push(40)
my_stack.push(50)
my_stack.print()

val = my_stack.pop()
print(val, "\n===")

my_stack.print()