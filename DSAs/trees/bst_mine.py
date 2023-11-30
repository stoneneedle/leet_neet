from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        outlist = []
        queue = deque()
        queue.append(self)

        level = 0
        while len(queue) > 0:
            for i in range(len(queue)):
                curr = queue.popleft()
                outlist.append(str(curr.val) + ' ') if curr != 'null' else outlist.append('null ')
                if curr != 'null':
                    if curr.left:
                        queue.append(curr.left)
                    else:
                        queue.append('null')
                    if curr.right:
                        queue.append(curr.right)
                    else:
                        queue.append('null')

            outlist.append('\n')
            level += 1

        return '\n'.join(''.join(outlist).split('\n')[:-2])


### A BST of n levels has (2^n)-1 values filled either with a value or null


### Search, insert, minValue, and remove

def search(root, target):
    if not root:
        return False

    if target > root.val:
        return search(root.right, target)
    elif target < root.val:
        return search(root.left, target)
    else:
        return True

# Insert a new node and return the root of the BST.
def insert(root, val):
    if not root:
        return TreeNode(val)

    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    return root


# Return the minimum value node of the BST.
def minValueNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr


# Remove a node and return the root of the BST.
def remove(root, val):
    if not root:
        return None

    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            minNode = minValueNode(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)
    return root

### Tree traversal (DFS)

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)

### BFS



def bfs(root):
    queue = deque()

    if root:
        queue.append(root)

    level = 0
    while len(queue) > 0:
        #print("level: ", level)
        for i in range(len(queue)):
            curr = queue.popleft()
            print(curr.val,' ', end='')
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        print()
        level += 1





### --------
#tn = TreeNode(4, TreeNode(3, TreeNode(2)), TreeNode(6, TreeNode(5), TreeNode(7)))
bst = TreeNode(val=4, left=TreeNode(val=3, left=TreeNode(2)), right=TreeNode(val=6, left=TreeNode(5), right=TreeNode(7)))

#bfs(bst)

print(bst)

# print("INORDER\n")
# inorder(tn)
# print("PREORDER\n")
# preorder(tn)
# print("POSTORDER\n")
# postorder(tn)
# print("BFS\n")
# bfs(tn)