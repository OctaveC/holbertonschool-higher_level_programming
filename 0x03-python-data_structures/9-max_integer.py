def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max = my_list[0]
        for ite in my_list:
            if ite > max:
                max = ite
    return max
