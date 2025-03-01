class Tree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def isBST(rootNode, lower=float('-inf'), upper=float('inf')):
    if not rootNode:
        return True
    
    if rootNode.value <= lower or rootNode.value >= upper:
        return False
    
    return (isBST(rootNode.left, lower, rootNode.value) and 
            isBST(rootNode.right, rootNode.value, upper))

def tree1():
    root = Tree(2)
    root.left = Tree(1)
    root.right = Tree(3)
    return root

def tree2():
    root = Tree(2)
    root.left = Tree(10)
    root.right = Tree(1)
    return root

tree0 = tree1()
tree2 = tree1()

print("Tree 1:")
if isBST(tree0):
    print("The tree is a valid BST.")
else:
    print("The tree is not a valid BST.")
    
print("Tree 2:")
if isBST(tree2):
    print("The tree is a valid BST.")
else:
    print("The tree is not a valid BST.")


