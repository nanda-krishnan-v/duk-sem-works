class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    
    def insertEle(self,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
    
    def display(self):
        current = self.head
        while current:
            print(current.data,end=" -> ")
            current = current.next
        print("None")
 
l = LinkedList()       
# l.insertEle(10)
# l.insertEle(40)
# l.insertEle(90)
l.display()