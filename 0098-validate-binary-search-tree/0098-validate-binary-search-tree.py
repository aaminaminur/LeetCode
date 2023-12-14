# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, lmin, rmax) -> bool:
            if not root:
                return True
            if root.val <= lmin or root.val >= rmax:
                return False
            left = helper(root.left, lmin, root.val)
            if left:
                right = helper(root.right, root.val, rmax)
            return left and right
        
        return helper(root, -10**10, 10**10)