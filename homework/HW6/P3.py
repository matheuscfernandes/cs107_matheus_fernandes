from random import sample
from time import time
from P2 import MinHeap
import heapq as h

class PriorityQueue:
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size

    def __len__(self):
        return len(self.elements)

    def __bool__(self):
        return len(self.elements) > 0

    def put(self, val):
        raise NotImplementedError # TODO

    def get(self):
        raise NotImplementedError # TODO

    def peek(self):
        raise NotImplementedError # TODO

def mergesortedlists(lists, pqclass=PriorityQueue):
    merged = []
    pq = pqclass(len(lists))
    for i, l in enumerate(lists): 
        pq.put((l.pop(0), i))

    while pq:
        ele, i = pq.get()
        merged.append(ele)
        if lists[i]:
            pq.put((lists[i].pop(0), i)) 

    return merged

def generatelists(n, length=20, dictionary_path='data/words.txt'):
    with open(dictionary_path, 'r') as f:
        words = [w.strip() for w in f.readlines()]
    lists = []
    for _ in range(n):
        lists.append(sorted(sample(words, length)))
    return lists


def timeit(ns=(10, 20, 50, 100, 200, 500), pqclass=PriorityQueue, n_average=5):
    elapsed = []
    for n in ns:
        timeaccum = 0
        for _ in range(n_average):
            lists = generatelists(n)
            start = time()
            merged = mergesortedlists(lists, pqclass)
            end   = time()
            timeaccum += end-start
        elapsed.append(timeaccum / n_average)
    return elapsed


class NaivePriorityQueue(PriorityQueue):
    def put(self,val):
        if len(self.elements) == self.max_size:
            raise IndexError('Full priority queue')
        self.elements.append(val)

    def get(self):
        ct=-1
        j=None
        if len(self.elements)==0:
            raise IndexError('Empty priority queue')
        for i in self.elements:
            ct+=1
            if (j is None): j=i;ind=ct
            if i<j:
                j=i
                ind=ct
        del self.elements[ind]
        return j

    def peek(self):
        j=None
        if len(self.elements)==0:
            raise IndexError('Empty priority queue')
        for i in self.elements:
            if (j is None): j=i
            if i<j:
                j=i
        return j        

class HeapPriorityQueue(PriorityQueue):
    def __init__(self,max_size) -> None:
        self.elements=MinHeap([])
        self.max_size = max_size

    def put(self, val):
        if self.elements.size == self.max_size:
            raise IndexError('Full priority queue')
        self.elements.heappush(val)
    def get(self):
        if self.elements.size==0:
            raise IndexError('Empty priority queue')
        return self.elements.heappop()

    def peek(self):
        if self.elements.size==0:
            raise IndexError('Empty priority queue')
        return self.elements.elements[0]

class PythonHeapPriorityQueue(PriorityQueue):
    def __init__(self,max_size) -> None:
        self.elements=[]
        self.max_size = max_size

    def put(self, val):
        if len(self.elements) == self.max_size:
            raise IndexError('Full priority queue')
        h.heappush(self.elements,val)
    def get(self):
        if len(self.elements)==0:
            raise IndexError('Empty priority queue')
        return h.heappop(self.elements)

    def peek(self):
        if len(self.elements)==0:
            raise IndexError('Empty priority queue')
        return h.nsmallest(1,self.elements)[0]

if __name__ == "__main__":
    q = NaivePriorityQueue(2)
    q = HeapPriorityQueue(2)
    q = PythonHeapPriorityQueue(2)


    q.put(1)
    q.put(2)
    print(q.peek())

    print(q.get())

    print(q.get())

    print(q.get())
