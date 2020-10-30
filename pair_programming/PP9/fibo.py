"""
Pair Programming Assignment #9
Collaborators: Ryan Liu, Haoxin Li, Matt C Fernandes
Iterators and Iterables for Fibonacci Sequence
"""

class FibonacciIterator():
    def __init__(self, value): 

        self.next_fib = 1
        self.curr_fib = 1
        self.counter = value

    def __next__(self): 
        if self.counter == 0:
            raise StopIteration
        self.counter -= 1

        next_fib = self.curr_fib + self.next_fib
        self.curr_fib = self.next_fib
        self.next_fib = next_fib

        return self.curr_fib

    def __iter__(self):
        return self

class Fibonacci():
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return FibonacciIterator(self.value)
            


fib = Fibonacci(10) # Create a Fibonacci iterator called fib that contains 10 terms
print(list(iter(fib))) # Iterate over the iterator and create a list.

