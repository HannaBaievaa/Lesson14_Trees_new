class Tree :
    def __init__(self, main_root):
        self.main_root = main_root
        self.left = None
        self.right = None

# функція додавання нового елементу
    def insert(self, data):
        if self.main_root:
            if data < self.main_root:
                if self.left is None:
                    self.left =Tree(data)
                else:
                    self.left.insert(data)
            elif data > self.main_root:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
        else:
            self.main_root.insert(data)

#функція додавання нового елементу зі списку
    def list_insert(self, lst):
        for n in lst:
            self.insert(n)