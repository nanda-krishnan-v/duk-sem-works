class Tree:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

def largestElement(root):
    if not root:
        return []
    
    queue = [root]
    max_levels = []
    
    while queue:
        level_max = max(node.val for node in queue)
        max_levels.append(level_max)
        queue = [child for node in queue for child in (node.left, node.right) if child]
    
    return max_levels

def tree1():
    root = Tree(1)
    root.left = Tree(3)
    root.right = Tree(2)
    root.left.left = Tree(5)
    root.left.right = Tree(3)
    root.right.right = Tree(9)
    return root


tree = tree1()
max_values = largestElement(tree)
print("Maximum values at each level:")
for level, max_val in enumerate(max_values):
    print(f"Level {level}: {max_val}")

