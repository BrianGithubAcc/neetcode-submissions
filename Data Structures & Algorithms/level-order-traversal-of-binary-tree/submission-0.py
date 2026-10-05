# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        k=[[]]
        def dfs(root,level):

            if root:
                if level<len(k):
                    k.append([])
                k[level].append(root.val)
                level+=1
                dfs(root.left,level) 
                dfs(root.right,level)
                
        dfs(root,0)
        return [l for l in k if l]          