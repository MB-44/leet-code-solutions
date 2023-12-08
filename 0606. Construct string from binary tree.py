# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self,root) -> str:

        # dfs - depth-first-search
        def dfs(root):
            if not root:
                return ""
            if root.right:
                return f"{root.val}({dfs(root.left)})({dfs(root.right)})"
            if root.left:
                return f"{root.val}({dfs.root.left})"
            return f"{root.val}"
        
        return dfs(root)