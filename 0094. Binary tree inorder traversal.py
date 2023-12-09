
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        
        def inOrder(root,result):
            if root is not None:
                inOrder(root.left,result)
                result.append(root.val)
                inOrder(root.right,result)

        result = []
        inOrder(root,result)
        return result
        