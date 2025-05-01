class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None

    def is_empty(self):
        return self.top is None

    def push(self,data):
        new_node=Node(data)
        new_node.next=self.top
        self.top=new_node

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        temp=self.top
        self.top=self.top.next
        return temp.data

    def peek(self):
        if self.is_empty():
            print("Stack is Empty")
            return None
        return self.top.data

    def display(self):
        current = self.top
        while current:
            print(current.data, end = " -> ")
            current = current.next
        print("None")


#Example Usage
stack=Stack()
stack.push(1)
stack.push(8)
stack.push(3)
stack.push(5)
stack.push(7)
stack.display()

print("Top : ",stack.peek())
print("Popped : ", stack.pop())
stack.display()
stack.is_empty()
