# Sharer: Ben Manning
# Coder: Matt C. Fernandes
# Listener: M. Elaine Cunha

class Sentence: # An iterable
    def __init__(self, text): 
        self.text = text
        self.words = text.split()

    def __iter__(self):
        for i in self.words:
            yield i 

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

if __name__ == '__main__':
    s=Sentence('I love you, for sentimental reasons.')

    for i in s:
        print(i)