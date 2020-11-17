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

    def _min(self,node):
        if node.left == None:
            return node
        node.left = self._min(node.left)

    def remove(self, key):
        self._root = self._remove(self._root, key)
    

    def _remove(self, node, key):
        if node == None:
            return None
        if key < node.key:
            node.left = self._remove(node.left,key)
        elif key> node.key:
            node.right = self._remove(node.right,key)
        if key == node.key:
            if node.right == None:
                return node.left
            if node.left == None:
                return node.right
            
            node_t=node
            node=self._min(node.right)
            node.right = self._removemin(node_t.right)
            node.left = node_t.left
            node.size = 1 + self._size(node.left) + self._size(node.right)

        else:
            raise KeyError(f'The \'{key}\' key does not belong in this BST.')

        return node


if __name__ == "__main__":
    
    print('\n----------------PART A DEMO---------------\n')
    
    t = BSTTable()
    t.put(5, 'd')
    t.put(1, 'b')
    t.put(2, 'c')
    t.put(0, 'a')

    # print(t._root)
    print('-----------------')

    # print(t._removemin(t._root))

    print('\n----------------PART B DEMO---------------\n')

    t = BSTTable()
    t.put(5, 'a')
    t.put(1, 'b')
    t.put(2, 'c')
    t.put(0, 'd')
    print(t._remove(t._root, 5))
    print('-----------------')
    print(t._remove(t._remove(t._root, 5), 1))
    print('-----------------')

    print(t._remove(t._root, 10))


from enum import Enum

class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

class DFSTraversal():
    def __init__(self, tree: BSTTable, traversalType: DFSTraversalTypes):
        self.tree=tree
        self.traversalType=traversalType

        if self.traversalType == DFSTraversalTypes.INORDER:
            self.inorder(self.tree)
        elif self.traversalType == DFSTraversalTypes.PREORDER:
            self.preorder(self.tree)
        elif self.traversalType == DFSTraversalTypes.POSTORDER:
            self.postorder(self.tree)
        else:
            raise Exception('unknown traversal type') 

    def __iter__(self):
        for i in self.values:
            ext = BSTNode(i[0],i[1])
            yield ext

    def __next__(self):
        try:
            val= self.values[self.index]

    def inorder(self, bst: BSTTable):
        # TODO: implement
        return

    def preorder(self, bst: BSTTable):
        # TODO: implement
        return

    def postorder(self, bst: BSTTable):
        # TODO: implement
        return

if __name__ == "__main__":
    
    print('\n----------------PART C DEMO ---------------\n')

    input_array = [(4, 'a'), (9, 'c'), (2, 'f'), (3, 'z'), (11, 'i'), (8, 'r')]
    bst = BSTTable()
    for key, val in input_array:
        bst.put(key, val)
    traversal = DFSTraversal(bst, DFSTraversalTypes.INORDER)
    for node in traversal:
        print(str(node.key) + ', ' + node.val)