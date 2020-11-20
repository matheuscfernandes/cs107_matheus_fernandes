from math import floor
from typing import List

class HeapAandB:
    def __init__(self, array: List[int]) -> None:
        self.elements = array
        self.size = len(array) # Number of elements in heap
        self.htype='min'
        self.build_heap()

    # index of left child of the node at idx
    def left(self, idx: int) -> int:
        return 2 * idx + 1

    # index of right child of the node at idx
    def right(self, idx: int) -> int:
        return 2 * idx + 2

    def parent(self, idx: int) -> int:
        return floor((idx - 1) / 2)

    def swap(self, idx1: int, idx2: int) -> None:
        tmp = self.elements[idx1]
        self.elements[idx1] = self.elements[idx2]
        self.elements[idx2] = tmp

    def to_string(self, prefix: str = "", idx: int = 0, left: bool = False) -> str:
        if self.size == 0:
            return '\\--'
        elif idx < self.size:
            buf = prefix
            if left:
                buf = buf + "|-- "
            else:
                buf = buf + "\\-- "
            # buf = buf + '\033[1m' + str(self.elements[idx]) + '\033[0m' + '\n'
            buf = buf + str(self.elements[idx]) + '\n' #use if above doesn't work

            new_prefix = prefix
            if left:
                new_prefix = new_prefix + "|   "
            else:
                new_prefix = new_prefix + "    "

            return buf + \
                    self.to_string(new_prefix, self.left(idx), True) + \
                    self.to_string(new_prefix, self.right(idx), False)
        else:
            return ''

    def __str__(self) -> str:
        return self.to_string()

    def __len__(self) -> str:
        return self.size

    def heapify(self, idx: int) -> None:
        if self.htype=='min':      
            if self.left(idx)<self.size and (self.elements[idx]>self.elements[self.left(idx)]):
                    self.swap(idx,self.left(idx))
                    self.heapify(self.left(idx))
            if self.right(idx)<self.size and (self.elements[idx]>self.elements[self.right(idx)]):
                    self.swap(idx,self.right(idx))
                    self.heapify(self.right(idx))

        elif self.htype=='max':
            if self.left(idx)<self.size and (self.elements[idx]<self.elements[self.left(idx)]):
                    self.swap(idx,self.left(idx))
                    self.heapify(self.left(idx))
            if self.right(idx)<self.size and (self.elements[idx]<self.elements[self.right(idx)]):
                    self.swap(idx,self.right(idx))
                    self.heapify(self.right(idx))

    def build_heap(self) -> None:
        for idx in range((self.size-1)//2,-1,-1):
            self.heapify(idx)
    
    def heappush(self, key: int) -> None:
        self.elements.append(key)
    
        self.size+=1
        current = self.size-1
        if self.htype == 'min':
            while self.elements[current] < self.elements[self.parent(current)]:
                if current<1:
                    return
                self.swap(self.parent(current),current)
                current = self.parent(current)

        if self.htype == 'max':
            while self.elements[current] > self.elements[self.parent(current)]:
                if current<1:
                    return
                self.swap(self.parent(current),current)
                current = self.parent(current)


    def heappop(self) -> int:
        popped = self.elements[0]
        self.elements[0]=self.elements[self.size-1]
        self.size-=1
        self.heapify(0)
        return popped

class Heap:
    def __init__(self, array: List[int]) -> None:
        self.elements = array
        self.size = len(array) # Number of elements in heap
        self.htype='min'

        self.build_heap()

    # index of left child of the node at idx
    def left(self, idx: int) -> int:
        return 2 * idx + 1

    # index of right child of the node at idx
    def right(self, idx: int) -> int:
        return 2 * idx + 2

    def parent(self, idx: int) -> int:
        return floor((idx - 1) / 2)

    def swap(self, idx1: int, idx2: int) -> None:
        tmp = self.elements[idx1]
        self.elements[idx1] = self.elements[idx2]
        self.elements[idx2] = tmp

    def to_string(self, prefix: str = "", idx: int = 0, left: bool = False) -> str:
        if self.size == 0:
            return '\\--'
        elif idx < self.size:
            buf = prefix
            if left:
                buf = buf + "|-- "
            else:
                buf = buf + "\\-- "
            # buf = buf + '\033[1m' + str(self.elements[idx]) + '\033[0m' + '\n'
            buf = buf + str(self.elements[idx]) + '\n' #use if above doesn't work

            new_prefix = prefix
            if left:
                new_prefix = new_prefix + "|   "
            else:
                new_prefix = new_prefix + "    "

            return buf + \
                    self.to_string(new_prefix, self.left(idx), True) + \
                    self.to_string(new_prefix, self.right(idx), False)
        else:
            return ''

    def __str__(self) -> str:
        return self.to_string()

    def __len__(self) -> int:
        return self.size

    # TODO: override this in your dervied classes
    def compare(self, a: int, b: int) -> bool:
        if self.htype == 'min':
            if a > b:
                return True
            else: 
                return False
    
        elif self.htype == 'max':
            if a < b:
                return True
            else: 
                return False
    

    def heapify(self, idx: int) -> None:
        if self.left(idx)<self.size and self.compare(self.elements[idx],self.elements[self.left(idx)]):
                self.swap(idx,self.left(idx))
                self.heapify(self.left(idx))
        if self.right(idx)<self.size and self.compare(self.elements[idx],self.elements[self.right(idx)]):
                self.swap(idx,self.right(idx))
                self.heapify(self.right(idx))

    def build_heap(self) -> None:
        for idx in range((self.size-1)//2,-1,-1):
            self.heapify(idx)

    def heappush(self, key: int) -> None:
        self.elements.append(key)
    
        self.size+=1
        current = self.size-1

        while self.compare(self.elements[self.parent(current)],self.elements[current]):
            if current<1:
                return
            self.swap(self.parent(current),current)
            current = self.parent(current)


    def heappop(self) -> int:
        popped = self.elements[0]
        self.elements[0]=self.elements[self.size-1]
        self.size-=1
        self.heapify(0)
        return popped

class MinHeap(Heap):
    def __init__(self, array: List[int]):
        self.elements = array
        self.size = len(array) # Number of elements in heap
        self.htype='min'
        self.build_heap()

class MaxHeap(Heap):
    def __init__(self, array: List[int]):
        self.elements = array
        self.size = len(array) # Number of elements in heap
        self.htype='max'
        self.build_heap()

if __name__ == "__main__":
    h = Heap([-1,0,0,15,23,1,2,3]) # The heap tree will be built during initialization
    print(h)
    h.heappush(-10)
    h.heappush(-11)
    h.heappush(5)
    h.heappush(25)
    print(h)
    print(h.heappop())
    print(h.heappop())
    print(h.heappop())
    print(h.heappop())
    print(h.heappop())
    print(h)

    mn = MinHeap([1,2,3,4,5])
    mx = MaxHeap([1,2,3,4,5])

    print(mn)
    print(mx)


