class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def traversal(self):
        if self.head is None:
            print("DLL not found")
        else:
            a = self.head
            while a is not None:
                print(a.data,end= " ")
                a = a.next
                
    def insertAtbeg(self,data):
        print()
        nn = Node(data)
        a = self.head
        a.prev = nn
        nn.next = a.next
        self.head = nn
        
    def insertATend(self,data):
        print()
        new_node = Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = new_node
        new_node.prev = a
        
    def insertAtpos(self,data,pos):
        print()
        new_node = Node(data)
        a = self.head
        for i in range(1,pos-1):
            a = a.next
        new_node.prev = a
        new_node.next = a.next
        a.next.prev = new_node
        a.next = new_node
        
    def deleteFromBeg(self):
        a = self.head
        self.head = a.next
        a.prev = None
        
    def deleteFromEnd(self):
        print()
        prev = self.head
        a = self.head.next
        while a.next is not None:
            a = a.next
            prev = prev.next
        prev.next = None
        a.prev = None
        
    def deleteFromPos(self,pos):
        print()
        prev = self.head
        a = self.head.next
        for i in range(1,pos-1):
            a = a.next
            prev = prev.next
        prev.next = a.next
        a.next.prev = prev
        a.next = None

dll = LinkedList()
n1 = Node(10)
dll.head = n1
n2 = Node(20)
n1.next = n2
n3 = Node(30)
n2.next = n3
n2.prev = n1
n4 = Node(40)
n3.next = n4
n3.prev = n2
n4.prev = n3

dll.insertAtbeg(5)
dll.insertATend(50)
dll.insertAtpos(25,3)
dll.deleteFromBeg()
dll.deleteFromEnd()
dll.deleteFromPos(3)
dll.traversal()
