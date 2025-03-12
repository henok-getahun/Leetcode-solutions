# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        return self.isMirror(root.left, root.right)
    
    def isMirror(self,node_1, node_2):
        if node_1 is None and node_2 is None:
            return True
        if node_1 is None or node_2 is None:
            return False

        return node_1.val == node_2.val and self.isMirror(node_1.left, node_2.right) and self.isMirror(node_1.right, node_2.left)
