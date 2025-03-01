class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def traversal(self):
        if self.head is None:
            print("SLL not exist")
        else:
            a = self.head
            while a is not None:
                print(a.data, end=" ")
                a = a.next
                
    def insertAtfront(self,data):
        print()
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node      
    
    def insertATend(self,data):
        print()
        new_node = Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = new_node           
        
    def insertAtposition(self,data,pos):
        print()
        new_node = Node(data)
        a = self.head
        for i in range(1,pos-1):
            a = a.next
        new_node.next = a.next 
        a.next = new_node
    
    def deleteFromBeg(self):
        a = self.head
        self.head = a.next
        a.next = None
        
    def deleteFromEnd(self):
        prev = self.head
        a = self.head.next
        while a.next is not None:
            a = a.next
            prev = prev.next
        prev.next = None
    
    def deleteAtpos(self,pos):
        prev = self.head
        a = self.head.next
        for i in range(1,pos-1):
            a = a.next
            prev = prev.next
        prev.next = a.next
        a.next = None        
        
sll = LinkedList()
n1 = Node(5)
sll.head = n1
n2 = Node(10)
n1.next = n2

sll.insertAtfront(10)
sll.insertATend(20)
sll.insertAtposition(90,1)
sll.deleteFromBeg()
sll.deleteFromEnd()
sll.deleteAtpos(1)
sll.traversal()

