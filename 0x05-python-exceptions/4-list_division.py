#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res_list = []
    res = 0
    for ite in range(list_length):
        try:
            res = my_list_1[ite] / my_list_2[ite]
        except TypeError:
            res = 0
            print("wrong type")
        except ZeroDivisionError:
            res = 0
            print("divison by 0")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            res_list.append(res)
    return res_list
