
from binary_tree import BinaryTree

def buildExpressionTree(exp):
    tree = BinaryTree('')
    stack = []
    stack.append(tree)
    current = tree

    for char in exp:
        if char == '(':
            current.insertLeft('')
            stack.append(current)
            current = current.leftChild
        elif char not in '+-*/()':
            current.key = int(char)
            parent = stack.pop()
            current = parent
        elif char in '+-*/':
            current.key = char
            current.insertRight('')
            stack.append(current)
            current = current.rightChild
        elif char == ')':
            current = stack.pop()
        else:
            raise ValueError

