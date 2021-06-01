#!/usr/bin/python3
""" Module for MyInt that inherits from Int """


class MyInt(int):
    """ MyInt Class inheriting from Int """
    pass

    def __eq__(self, other_int):
        """ Rebel instance method """
        return int(self) != int(other_int)

    def __ne__(self, other_int):
        """ Rebel instance method """
        return int(self) == int(other_int)
