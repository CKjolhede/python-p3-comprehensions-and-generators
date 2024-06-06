#!/usr/bin/env python3

def return_evens(num_list):
    newList = [num for num in num_list if (num % 2)== 0]
    return newList

def make_exclamation(sentence_list):
    sentences = [sentence + "!" for sentence in sentence_list]
    return sentences