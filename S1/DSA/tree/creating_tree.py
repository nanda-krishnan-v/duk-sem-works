class Node:
    def __init__(self,value):
        self.value = value
        self.children = []
    
class Tree:
    def __init__(self,root_value):
        self.root = Node(root_value)
        
    def find_node(self,value,current_node = None):
        #finds the node in the tree with the given value#
        if current_node is None:
            current_node = self