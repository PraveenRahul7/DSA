class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class TreeTraversal:
    def __init__(self, root: TreeNode):
        self.root = root

    def recursive_inorder(self, node: TreeNode, result = None):
        """Recursive Inorder Traversal."""
        if result is None:
            result = []
        if node:
            self.recursive_inorder(node.left, result)
            result.append(node.val)
            self.recursive_inorder(node.right, result)
        return result
        

    def recursive_preorder(self, node: TreeNode, result = None):
        """Recursive Preorder Traversal."""
        if result is None:
            result = []
        if node:
            result.append(node.val)
            self.recursive_preorder(node.left, result)
            self.recursive_preorder(node.right, result)
        return result


    def recursive_postorder(self, node: TreeNode, result = None):
        """Recursive Postorder Traversal."""
        if result is None:
            result = []
        if node is None:
            self.recursive_postorder(node.left, result)
            self.recursive_postorder(node.right, result)
            result.append(node.val)
        return result



    def iterative_inorder(self):
        """Iterative Inorder Traversal."""
        q = []
        res = []

    def iterative_preorder(self):
        """Iterative Preorder Traversal."""
        stack = []
        res = []
        stack.append(self.root)
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right is not None:
                stack.append(curr.right)
            if curr.left is not None:
                stack.append(curr.left)
        return res

    def iterative_postorder(self):
        """Iterative Postorder Traversal."""
        pass


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)