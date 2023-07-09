class Tree :
    def __init__(self, main_root):
        self.main_root = main_root
        self.left = None
        self.right = None

    # Пошук мінімального значення
    def find_min(self):
        if self.left is None:
            return self.main_root
        return self.left.find_min()

    # Пошук максимального значення
    def find_max(self):
        if self.right is None:
            return self.main_root
        return self.right.find_max()