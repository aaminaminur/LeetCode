# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def is_valid(root, minval, maxval) -> bool:
            if not root:
                return True
            if root.val <= minval or root.val >= maxval:
                return False
            ls = is_valid(root.left, minval, root.val)
            rs = is_valid(root.right, root.val, maxval)
            
            return ls and rs
        
        return is_valid(root, -10**10, 10**10)
