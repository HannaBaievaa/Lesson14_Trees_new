class Tree:
    def __init__(self, main_root):
        self.main_root = main_root
        self.left = None
        self.right = None

#видалення елементу
    def delete_node(root, key):
        if root is None:
            return root
        if key < root.main_root:
            root.left = root.left.delete_node(key)
        elif key > root.main_root:
            root.right = root.right.delete_node(key)
        else:
            if root.left is None:
                temp = root.right
                return temp
            elif root.right is None:
                temp = root.left
                return temp
            temp = root.right.minValueNode()
            root.main_root = temp.main_root
            root.right = root.right.deleteNode(temp.main_root)
        return root