class node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

class Bstree:
    def __init__(self):
        self.root = None

    def insert(self, p, x):
        if p is None:
            return node(x)
        if x < p.data:
            p.left = self.insert(p.left, x)
        else:
            p.right = self.insert(p.right, x)
        return p

    def inorder(self, p):
        if p is None:
            return
        self.inorder(p.left)
        print(p.data)
        self.inorder(p.right)


bs = Bstree()


bs.root = bs.insert(bs.root, 10)
bs.root = bs.insert(bs.root, 5)
bs.root = bs.insert(bs.root, 15)
bs.root = bs.insert(bs.root, 20)
bs.root = bs.insert(bs.root, 18)
bs.root = bs.insert(bs.root, 8)
bs.root = bs.insert(bs.root, 9)
bs.root = bs.insert(bs.root, 7)




bs.inorder(bs.root)
