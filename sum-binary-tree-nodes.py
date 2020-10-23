#From unit assessment
# on CodeSignal
#Given the root of a binary tee where each node contains an ineger, determine the sum of all of the integer values in the tree.

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def tree_paths_sum(root):
    sum = sumRight = sumLeft = 0
    
    if root.value == None:
        return 0
    
    else:
        if root.left != None:
            sumLeft = tree_paths_sum(root.left)
        if root.right != None:
            sumRight = tree_paths_sum(root.right)
        sum = root.value + sumLeft + sumRight
    
    return sum