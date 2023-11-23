class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val) + ' ' + str(self.left if self.left else '') + str(self.right if self.right else '')
[]
t = TreeNode(1)
print(t.val)