class TreeNode:
    def __init__(self,data = None, left = None,right = None):
        self.data = data
        self.left = left 
        self.right = right

def inorder_Traversal(node):
    if node is None:
        return 
    inorder_Traversal(node.left)
    print(node.data)
    inorder_Traversal(node.right)

def preorder_Traversal(node):
    if node is None:
        return
    print(node.data)
    preorder_Traversal(node.left)
    preorder_Traversal(node.right)

def postorder_Traversal(node):
    if node is None:
        return
    postorder_Traversal(node.left)
    postorder_Traversal(node.right)
    print(node.data)

def isbst(node,min_val,max_val):
    if node is None:
        return True
    if node.data < min_val or node.data > max_val:
        return False
    is_left_valid = isbst(node.left,min_val,node.data)
    if not is_left_valid: 
        return False
    is_right_valid = isbst(node.right,node.data,max_val)
    if not is_right_valid:
        return False
    return True

n1 = TreeNode(10)
n2 = TreeNode(6)
n3 = TreeNode(15)
n4 = TreeNode(4)
n5 = TreeNode(7)

n1.left = n2
n1.right = n3
n2.left = n4
n3.right = n5 

node = n1

print(isbst(node,float('-inf') ,float('+inf')))