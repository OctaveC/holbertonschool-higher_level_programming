#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if ite == search else ite for ite in my_list]
