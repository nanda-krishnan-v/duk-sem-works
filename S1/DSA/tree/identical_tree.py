class Tree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def isIdentical(aRoot,bRoot):
    if aRoot == None and bRoot == None:
        return True
    if aRoot == None or bRoot == None:
        return False
    
    return (aRoot.value == bRoot.value and 
            isIdentical(aRoot.left,bRoot.left) and 
            isIdentical(aRoot.right,bRoot.right))

def Tree1():
    rootNode = Tree(1)
    rootNode.left = Tree(2)
    rootNode.right = Tree(3)
    rootNode.left.left = Tree(4)
    rootNode.left.right = Tree(5)
    return rootNode
        
def Tree2():
    rootNode = Tree(1)
    rootNode.left = Tree(2)
    rootNode.right = Tree(3)
    rootNode.left.left = Tree(4)
    rootNode.left.right = Tree(5)
    return rootNode

def Tree3():
    rootNode = Tree(1)
    rootNode.left = Tree(24)
    rootNode.right = Tree(23)
    rootNode.left.left = Tree(24)
    rootNode.left.right = Tree(5)
    return rootNode 

firstTree = Tree1()
secondTree = Tree2()
thirdTree = Tree3()

identity = isIdentical(firstTree,secondTree)
Random = isIdentical(firstTree,thirdTree)

print("Round One: ")
if identity:
    print("The Trees are Identical!!")
else:
    print("OOPS, They are not Identical")

print("Round Two: ")
if Random:
    print("The Trees are Identical!!")
else:
    print("OOPS, They are not Identical")