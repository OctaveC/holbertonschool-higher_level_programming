#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for ite in list(a_dictionary.keys()):
        if a_dictionary[ite] == value:
            del(a_dictionary[ite])
    return a_dictionary
