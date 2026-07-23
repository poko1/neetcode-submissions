# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        c = [0]
        c[0] = 0
        def dfs(root,mx):
            if not root:
                return
            if root.val>=mx:
                c[0]+=1
            mx = max(root.val,mx)
            dfs(root.left,mx)
            dfs(root.right,mx)

        dfs(root,root.val)
        return c[0]

        