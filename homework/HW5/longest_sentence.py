from linked_list import *

def get_list_of_sentences(chapter1='swansway-chapter1.txt'):
    def to_sentences(p):
            for delimiter in '.?!': p = p.replace(delimiter, '|')
            return [s.strip('\" ') for s in p.split('|')]
    with open(chapter1, 'r', encoding='UTF-8') as f:
        paragraphs = f.readlines()

    sentences = [s for p in paragraphs for s in to_sentences(p) if len(s) > 1]
    list_of_sentences = Nil()
    for s in sentences[::-1]:
        list_of_sentences = list_of_sentences.prepend(s)

    return list_of_sentences

 
def longest_sentence():
    list_of_sentences = get_list_of_sentences()
    def smaller(a, b): # our "combine" function
        return a if a < b else b
    list_of_sentences.reduce_right(smaller)

longest_sentence()