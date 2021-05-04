def divisible_by_2(my_list=[]):
    new_list = []
    for ite in my_list:
        if ite % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
