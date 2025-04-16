class DoublyNode: 
    def __init__(self, data): 
        self.data = data 
        self.next = None 
        self.prev = None 

class DoublyLinkedList: 
    def __init__(self): 
        self.head = None 
        self.tail = None 
  
    def insert_at_beginning(self, data): 
        new_node = DoublyNode(data) 
        if self.head is None: 
            self.head = self.tail = new_node 
        else: 
            new_node.next = self.head 
            self.head.prev = new_node 
            self.head = new_node 
            
    def delete_node(self):
        if self.head is None:
            return None
        current = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        del current
        return self.head
    
    def traverse_forward(self): 
        current = self.head 
        while current: 
            print(current.data, end=" <-> " if current.next else "")
            current = current.next 
        print()
    
    
Node1=DoublyNode(10)
Node2=DoublyNode(20)
Node3=DoublyNode(30)
Node1.prev=None
Node1.next=Node2
Node2.prev=Node1
Node2.next=Node3
Node3.prev=Node2
Node3.next=None

print("Traversing the list in forward direction: \n")
dll = DoublyLinkedList()
dll.head = Node1
dll.tail = Node3
dll.traverse_forward()

dll.insert_at_beginning(40)
print("After inserting Numbers in the begining: \n")
dll.traverse_forward()


dll.delete_node()
print("After deleting the first node: \n")
dll.traverse_forward()
