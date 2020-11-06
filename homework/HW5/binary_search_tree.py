class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left = None
        self.right = None
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
        try:
            if node.key > key:
                node.left = self._put(node.left,key,val)
            elif node.key < key:
                node.right = self._put(node.right,key,val)
            else:
                node.val=val
            return node

        except:
            return BSTNode(key,val)

    def _get(self, node, key):
        try:
            if node.key > key:
                val = self._get(node.left,key)
            elif node.key < key:
                val = self._get(node.right,key)
            else: 
                val = node.val
                print(val)
            return val
        except:
            raise KeyError(f"Nothing found for {key} key.")

    @staticmethod
    def _size(node):
        return node.size if node else 0


greektoroman = BSTTable()
greektoroman.put('Athena',    'Minerva')
greektoroman.put('Eros',      'Cupid')
greektoroman.put('Aphrodite', 'Venus')
greektoroman.get('Eros')

print(greektoroman)


