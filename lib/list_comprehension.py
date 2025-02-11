#!/usr/bin/env python3

def return_evens(num_list):
    list = []
    for n in num_list:
        if n % 2 == 0 :
            list.append(n)
    return list

def make_exclamation(sentence_list):
    for i in range(len(sentence_list)):
        sentence_list[i] = sentence_list[i] + "!"
    return sentence_list