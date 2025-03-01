class Tree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def ArrayToBST(array1):
    if not array1:
        return None
    mid = len(array1) // 2
    rootNode = Tree(array1[mid])
    rootNode.left = ArrayToBST(array1[:mid])
    rootNode.right = ArrayToBST(array1[mid+1:])
    return rootNode

def preOrderTraversal(Node):
    if Node:
        print(Node.value, end=" ")
        preOrderTraversal(Node.left)
        preOrderTraversal(Node.right)  
    
array = [1,2,3,4,5,6,7]        
b1 = ArrayToBST(array)     
preOrderTraversal(b1)