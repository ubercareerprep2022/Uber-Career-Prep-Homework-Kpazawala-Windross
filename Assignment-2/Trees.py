from re import X


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        n = self.Node(value)
        if (self.root == None):
            self.root = n
        else:
            return self.insert_helper(value, self.root)

    def insert_helper(self, value, n):
        if(value == n.data):
            return False
        else:
            if(value > n.data):

                if (n.right == 0):
                    n.right = self.Node(value)
                    n.right.parent = n
                else:
                    Tree.insert_helper(self, value, n.right)
            else:
                if (n.left == 0):
                    n.left = self.Node(value)
                    n.left.parent = n
                else:
                    Tree.insert_helper(self, value, n.left)
        return True
    
    def printInOrder(self):
        self.helper_printInOrder(self.root)
        print()
    def helper_printInOrder(self, n):
        if(n != 0):
            Tree.helper_printInOrder(self, n.left)
            print(n.data, end=" ")
            Tree.helper_printInOrder(self, n.right)

    def printPreOrder(self):
        self.helper_printPreOrder(self.root)
        print()
    def helper_printPreOrder(self, n):
        if(n != 0):
            print(n.data, end=" ")
            Tree.helper_printPreOrder(self, n.left)
            Tree.helper_printPreOrder(self, n.right)

    def printPostOrder(self):
        self.helper_printPostOrder(self.root)
        print()
    def helper_printPostOrder(self, n):
        if(n != 0):
            Tree.helper_printPostOrder(self, n.left)
            Tree.helper_printPostOrder(self, n.right)
            print(n.data, end=" ")


    class Node:
        def __init__(self, data = None, parent = 0, left = 0, right = 0):
            self.data = data
            self.parent = parent
            self.left = left
            self.right = right

x = Tree()
x.insert(1)
x.insert(7)
x.insert(17)
x.insert(6)
x.insert(3)

x.printInOrder()
x.printPreOrder()
x.printPostOrder()




