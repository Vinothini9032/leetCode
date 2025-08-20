# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        parent=None
        cur=root
        while cur and cur.val!=key:
            parent=cur
            if key<cur.val:
                cur=cur.left
            elif key>cur.val:
                cur=cur.right
        if not cur:
            return root
        
        if cur.left and cur.right:
            successor=cur
            succ=cur.right
            while succ.left:
                successor=succ
                succ=succ.left
            cur.val=succ.val
            cur,parent=succ,successor
        child=cur.left if cur.left else cur.right
        if not parent:
            return child
        if parent.left==cur:
            parent.left=child
        else:
            parent.right=child
        return root




        