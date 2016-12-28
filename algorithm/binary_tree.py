
class BinaryTree():
    def __init__(self, item):
        self.key = item
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, item):
        if self.leftChild is None:
            self.leftChild = BinaryTree(item)
        else:
            tree = BinaryTree(item)
            tree.leftChild = self.leftChild
            self.leftChild = tree

    def insertRight(self, item):
        if self.rightChild is None:
            self.rightChild = BinaryTree(item)
        else:
            tree = BinaryTree(item)
            tree.rightChild = self.rightChild
            self.rightChild = tree