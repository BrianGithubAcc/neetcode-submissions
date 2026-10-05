# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def explore(root,level):
            if root:
                return max(explore(root.left,level+1),explore(root.right,level+1))
            else:
                return level
        
        return explore(root,0)