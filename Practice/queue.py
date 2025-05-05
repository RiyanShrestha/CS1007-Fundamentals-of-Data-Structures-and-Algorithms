class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None

class queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def is_empty(self):
        return self.front is None

    def enqueue(self,data):
        new_node=Node(data)
        if self.rear is None:
            self.front=self.rear=new_node
        else:
            self.rear.next=new_node
            new_node=self.rear
        print(f"Enqueued: {data}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        removed_data=self.front.data
        self.front=self.front.next
        if self.front is None:
            self.rear=None
        print(f"Dequeued: {removed_data}")

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.front.data

    def display(self):
        current = self.front
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Queue elements:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        
#example usage
q=queue()
q.enqueue(10)
q.enqueue(80)
q.enqueue(30)
q.enqueue(70)
q.enqueue(160)
q.peek()
q.display()
q.dequeue()
q.display()
