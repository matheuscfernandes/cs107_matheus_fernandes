class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left, self.right = None, None
        self.size = 1

    def __str__(self):
        return f'BSTNode({self.key}, {self.val})' + \
               '\n|\n|-(L)->' + '\n|      '.join(str(self.left ).split('\n')) + \
               '\n|\n|-(R)->' + '\n|      '.join(str(self.right).split('\n'))


class BSTTable:
    def __init__(self):
        self._root = None

    def __str__(self):
        return str(self._root)

    def __len__(self):
        return self._size(self._root)

    def put(self, key, val):
        self._root = self._put(self._root, key, val)

    def get(self, key):
        return self._get(self._root, key)

    def _put(self, node, key, val):
        if not node: 
            return BSTNode(key, val)
        if   key < node.key:
            node.left  = self._put(node.left,  key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _get(self, node, key):
        if not node:
            raise KeyError(f'key not found: {key}')
        if   key < node.key:
            return self._get(node.left,  key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val

    @staticmethod
    def _size(node):
        return node.size if node else 0

    def _removemin(self,node):
        if node.left == None:
            return node.right
        node.left = self._removemin(node.left)
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def remove(self, key):
        self._root = self._remove(self._root, key)

    def _remove(self, node, key):
        if node == None:
            return None
        if key < node.key:
            node.left = self._remove(node.left,key)
        elif key> node.key:
            node.right = self._remove(node.right,key)
        else:
            if node.right == None:
                return node.left
            if node.left == None:
                return node.right
            
            node_t = node
            node - min

if __name__ == "__main__":
    t = BSTTable()
    t.put(5, 'd')
    t.put(1, 'b')
    t.put(2, 'c')
    t.put(0, 'a')

    print(t._root)

    print(t._removemin(t._root))


    t = BSTTable()
    t.put(5, 'a')
    t.put(1, 'b')
    t.put(2, 'c')
    t.put(0, 'd')

    print(t._remove(t._remove(t._root, 5), 1))

    print(t._remove(t._root, 10))


