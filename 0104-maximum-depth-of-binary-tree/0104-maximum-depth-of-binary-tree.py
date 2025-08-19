# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depths(root,depth):
            if not root:
                return 0
            left_depth=depths(root.left,depth+1)
            right_depth=depths(root.right,depth+1)
            return 1+max(left_depth,right_depth)
        return depths(root,0)
        