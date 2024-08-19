#!/usr/bin/env python3


def return_evens(numbers):
    return [num for num in numbers if num % 2 == 0]

def make_exclamation(sentence_list):
    return[ sentence_list + "!" for sentence_list in sentence_list]