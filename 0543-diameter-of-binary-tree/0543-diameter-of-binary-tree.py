# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia = 0
        def helper(root):
            if not root:
                return -1
            
            lh = helper(root.left)
            rh = helper(root.right)
            
            self.dia = max(self.dia, lh+rh+2)
            
            return max(lh, rh) + 1
            
        helper(root)
        return self.dia