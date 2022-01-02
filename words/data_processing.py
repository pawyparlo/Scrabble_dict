# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import codecs

from itertools import permutations

def print_words(func):

    def inside_wrapper(*args, **kwargs):
        result = list(func(*args, **kwargs))
        return '''Words you can arrange: {}'''.format(sorted(result, key=len))

    return inside_wrapper

def open_txt_file(filename: str):
    with codecs.open(filename, 'r', 'utf-8') as f:
        data = set(f.read().splitlines())
    return data

@print_words
def find_word(list_of_words, word):
    words = set()

    for i in range(1, len(word) + 1):
        var = list(permutations(word, i))
        var = {''.join(list(x)) for x in var}
        for x in var.intersection(list_of_words):
            words.add(''.join(list(x)))
    return words









