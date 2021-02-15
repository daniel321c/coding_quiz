# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.total = 0

        self.getNumber(root, 0)
        return self.total

    def getNumber(self, node, carry):
        if(node is None):
            return
        if(node.left is None and node.right is None):
            self.total += carry*10 + node.val
            return
        if(node.left is not None):
            self.getNumber(node.left, carry*10 + node.val)
        if(node.right is not None):
            self.getNumber(node.right, carry*10+node.val)
