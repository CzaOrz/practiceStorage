class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def pre(root):
    if root == None:
        return
    print(root.value)
    pre(root.left)
    pre(root.right)


def mid(root):
    if root == None:
        return
    mid(root.left)
    print(root.value)
    mid(root.right)


def aft(root):
    if root == None:
        return
    aft(root.left)
    aft(root.right)
    print(root.value)


# root = Node('D', Node('B', Node('A'), Node('C')), Node('E', right=Node('G', Node('F'))))

root = last = Node('A')
for i in 'BCDEFG':
    if last.left is None:
        last.left = Node(i)
        continue
    if last.right is None:
        last.right = Node(i)
        continue
    last = last.left
    last.left = Node(i)
# pre(tree)
# mid(tree)
print('前序遍历：')
pre(root)
print('\n')
print('中序遍历：')
mid(root)
print('\n')
print('后序遍历：')
aft(root)
