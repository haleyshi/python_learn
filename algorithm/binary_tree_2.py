def BinaryTree(item):
    return [item, [], []]

def insertLeft(tree, item):
    leftChild = tree.pop(1)
    if leftChild:
        tree.insert(1, [item, leftChild, []])
    else:
        tree.insert(1, BinaryTree(item))

def insertRight(tree, item):
    rightChild = tree.pop(2)
    if rightChild:
        tree.insert(2, [item, [], rightChild])
    else:
        tree.inser(2, BinaryTree(item))

def getLeft(tree):
    return tree[1]

def getRight(tree):
    return tree[2]

