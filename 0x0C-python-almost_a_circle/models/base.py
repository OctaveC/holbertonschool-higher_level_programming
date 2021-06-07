#!/usr/bin/python3
""" Module for Base Class """
import json
import csv


class Base:
    """ Class serving as a base for multiple shapes """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string """
        if json_string is None or len(json_string) is 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        dic = []
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as opening:
            if list_objs:
                for ite in list_objs:
                    dic.append(ite.to_dictionary())
            opening.write(cls.to_json_string(dic))

    @classmethod
    def load_from_file(cls):
        """returns a list of instances """
        try:
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as op:
                l = cls.from_json_string(op.read())
                return [cls.create(**dic) for dic in l]
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ is "Rectangle":
            new = cls(1, 1, 0, 0, 0)
        elif cls.__name__ is "Square":
            new = cls(1, 0, 0, 0)
        new.update(new, **dictionary)
        return new

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes in CSV """
        data = []
        if list_objs is not None:
            for obj in list_objs:
                if cls.__name__ is "Rectangle":
                    data.append([obj.id, obj.width, obj.height, obj.x, obj.y])
                if cls.__name__ is "Square":
                    data.append([obj.id, obj.size, obj.x, obj.y])
            with open(cls.__name__ + ".csv", "w", newline="") as opening:
                write = csv.writer(opening)
                write.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes in CSV """
        try:
            with open(cls.__name__ + ".csv", "r") as opening:
                read = csv.reader(opening)
                dic = []
                for row in read:
                    if cls.__name__ is "Rectangle":
                        data = {"id": int(row[0]), "width": int(row[1]),
                                "height": int(row[2]), "x": int(row[3]),
                                "y": int(row[4])}
                    elif cls.__name__ is "Square":
                        data = {"id": int(row[0]), "size": int(row[1]),
                                "x": int(row[2]), "y": int(row[3])}
                    dic.append(cls.create(**data))
                return dic
        except FileNotFoundError:
            return []
