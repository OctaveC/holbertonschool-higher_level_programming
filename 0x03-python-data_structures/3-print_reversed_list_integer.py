def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        for ite in my_list[::-1]:
            print("{}".format(ite))