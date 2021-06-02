#!/usr/bin/python3
""" Module for Student """


class Student():
    """ A student class that defines a student. """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of Student instance """
        if type(attrs) is list and all([type(ite) is str for ite in attrs]):
            return {key: v for key, v in self.__dict__.items() if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance. """
        for key, value in json.items():
            self.__dict__[key] = value
