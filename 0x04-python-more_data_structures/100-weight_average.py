#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) <= 0:
        return None
    weight, total = 0, 0
    for (ite1, ite2) in my_list:
        weight += ite2
        total += ite2 * ite1
    return total/weight
