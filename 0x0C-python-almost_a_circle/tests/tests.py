#!/usr/bin/python3
""" Contains tests for all our classes """


import unittest
import json
from models import base
from models import rectangle
from models import square
Base = base.Base
Rectangle = rectangle.Rectangle
Square = square.Square


class TestsForBase(unittest.TestCase):
    """ Tests for the Base Class """

    def test_auto_id(self):
        """ Testing auto id """
        base = Base()
        self.assertEqual(base.id, 1)

    def test_next_id(self):
        """ Testing second auto id """
        base_2 = Base()
        self.assertEqual(base_2.id, 2)

    def test_id_set(self):
        """ Testing id as not None """
        base_413 = Base(413)
        self.assertEqual(base_413.id, 413)

    def test_id_negative(self):
        """ Testing id as negative """
        base_nega = Base(-1)
        self.assertEqual(base_nega.id, -1)

    def test_multiple_args(self):
        """ Testing too many args """
        with self.assertRaises(TypeError):
            err = Base(1, 2)

    def test_nb_priv(self):
        """ Testing nb_objects """
        base_3 = Base(3)
        with self.assertRaises(AttributeError):
            print(base_3.nb_objects)
        with self.assertRaises(AttributeError):
            print(base_3.__nb_objects)

    def test_to_json_string(self):
        """ Testing json string """
        Base._Base__nb_objects = 0
        json1 = {"id": 7, "width": 4, "height": 7, "x": 2, "y": 9}
        json2 = {"id": 3, "width": 12, "height": 9, "x": 0, "y": 0}
        json_s = Base.to_json_string([json1, json2])
        self.assertTrue(type(json_s) is str)
        thing = json.loads(json_s)
        self.assertEqual(thing, [json1, json2])

    def test_to_json_empty(self):
        """ Test for empty list """
        json_s = Base.to_json_string([])
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_json_string_none(self):
        """ Testing None to json """
        json_s = Base.to_json_string(None)
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_from_json_string(self):
        """ Testing standard case for from_json_string """
        json_str = '[{"id": 6, "width": 2, "height": 8, "x": 0, "y": 2}, \
{"id": 3, "width": 4, "height": 2, "x": 6, "y": 1}]'
        json_l = Base.from_json_string(json_str)
        self.assertEqual(len(json_l), 2)
        self.assertTrue(type(json_l) is list)
        self.assertTrue(type(json_l[0]) is dict)
        self.assertTrue(type(json_l[1]) is dict)
        self.assertEqual(json_l[0],
                         {"id": 6, "width": 2, "height": 8, "x": 0, "y": 2})
        self.assertEqual(json_l[1],
                         {"id": 3, "width": 4, "height": 2, "x": 6, "y": 1})

    def test_from_json_string_empty(self):
        """ Testing from_json_string with an empty string """
        self.assertEqual([], Base.from_json_string(""))

    def test_from_json_string_None(self):
        """ Testing from_json_string with none string """
        self.assertEqual([], Base.from_json_string(None))


class TestsforRectangle(unittest.TestCase):
    """ Tests for the Rectangle class """

    @classmethod
    def setUpClass(cls):
        """ Initial Setup """
        Base._Base__nb_objects = 0
        cls.Rec1 = Rectangle(5, 5)
        cls.Rec2 = Rectangle(4, 5, 6)

    def test_id(self):
        """ Testing for setting ID """
        self.assertEqual(self.Rec1.id, 1)
        self.assertEqual(self.Rec2.id, 2)

    def test_width(self):
        """ Testing for standard width """
        self.assertEqual(self.Rec1.width, 5)
        self.assertEqual(self.Rec2.width, 4)

    def test_height(self):
        """ Testing for standard height """
        self.assertEqual(self.Rec1.height, 5)
        self.assertEqual(self.Rec2.height, 5)

    def test_x(self):
        """ Testing for standard x """
        self.assertEqual(self.Rec1.x, 0)
        self.assertEqual(self.Rec2.x, 6)

    def test_y(self):
        """ Testing for standard y """
        self.assertEqual(self.Rec1.y, 0)
        self.assertEqual(self.Rec2.y, 0)

    def test_missing_arg_width(self):
        """ Testing missing argument """
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_missing_arg_height(self):
        """ Testing missing height """
        with self.assertRaises(TypeError):
            r = Rectangle(8)

    def test_width_type(self):
        """ Testing not int for width """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("HEY", 3)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(False, 3)

    def test_height_type(self):
        """ Testing not int for height """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(2, "ooooooooo")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(4, True)

    def test_x_type(self):
        """ Testing not int for x """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(2, 2, "who")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(4, 4, True)

    def test_y_type(self):
        """ Testing not int for y """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(2, 2, 2, "lives")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(4, 4, 4, True)

    def test_width_value(self):
        """ ints <= 0 for width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-2, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 12)

    def test_height_value(self):
        """ Testing ints <= 0 for height """
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(6, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(2, 0)

    def test_x_value(self):
        """ Testing ints < 0 for x """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(2, 6, -8)

    def test_y_value(self):
        """ Testing ints <= 0 for y """
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(1, 1, 1, -1)

    def test_area(self):
        """ Testing area """
        self.assertEqual(self.Rec1.area(), 25)
        self.assertEqual(self.Rec2.area(), 20)

    def test_area_args(self):
        """ Testing too many args for area """
        with self.assertRaises(TypeError):
            r = self.Rec1.area(2)

    def test_display_too_many_args(self):
        """ Testing display with too many args """
        with self.assertRaises(TypeError):
            self.Rec1.display(2)

    def test_str(self):
        """Test the __str__ method"""
        self.assertEqual(str(self.Rec1), "[Rectangle] (1) 0/0 - 5/5")
        self.assertEqual(str(self.Rec2), "[Rectangle] (2) 6/0 - 4/5")

    def test_update_args(self):
        """ Testing the update method with *args """
        r = Rectangle(2, 2, 0, 0, 2)
        self.assertEqual(str(r), "[Rectangle] (2) 0/0 - 2/2")
        r.update(12)
        self.assertEqual(str(r), "[Rectangle] (12) 0/0 - 2/2")
        r.update(42, 3)
        self.assertEqual(str(r), "[Rectangle] (42) 0/0 - 3/2")
        r.update(42, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (42) 0/0 - 2/3")
        r.update(42, 2, 3, 7)
        self.assertEqual(str(r), "[Rectangle] (42) 7/0 - 2/3")
        r.update(42, 2, 3, 7, 92)
        self.assertEqual(str(r), "[Rectangle] (42) 7/92 - 2/3")

    def test_update_args_setter(self):
        """ Testing that the update method uses setters """
        r = Rectangle(2, 2, 0, 0, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(2, "hi!")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(2, 2, "meh")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(2, 2, 2, "truc")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(2, 2, 2, 2, "turc")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(2, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(2, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(2, 2, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(2, 2, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(2, 2, 2, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(2, 2, 2, 2, -1)

    def test_update_too_many_args(self):
        """ Testing too many args for update """
        r = Rectangle(2, 2, 0, 0, 2)
        r.update(2, 3, 3, 2, 2, 2)
        self.assertEqual(str(r), "[Rectangle] (2) 2/2 - 3/3")

    def test_update_no_args(self):
        """ Testing no args for update"""
        r = Rectangle(2, 2, 3, 1, 2)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (2) 3/1 - 2/2")

    def test_mix_args_kwargs(self):
        """ Testing output for mixed args and kwargs """
        r = Rectangle(2, 2, 0, 0, 2)
        r.update(1, 1, 1, 1, 1, width=3, height=3, x=3, y=3, id=3)
        self.assertEqual(str(r), "[Rectangle] (1) 1/1 - 1/1")


class TestsForSquare(unittest.TestCase):
    """ Test for the Square class"""

    @classmethod
    def setUpClass(cls):
        """ Setup """
        Base._Base__nb_objects = 0
        cls.squa1 = Square(4)
        cls.squa2 = Square(5, 6)

    def test_id(self):
        """ Testing for standard id """
        self.assertEqual(self.squa1.id, 1)
        self.assertEqual(self.squa2.id, 2)

    def test_size(self):
        """ Testing for standard size"""
        self.assertEqual(self.squa1.size, 4)
        self.assertEqual(self.squa2.size, 5)

    def test_width(self):
        """ Testing for standard width """
        self.assertEqual(self.squa1.width, 4)
        self.assertEqual(self.squa2.width, 5)

    def test_height(self):
        """ Testing for standard height """
        self.assertEqual(self.squa1.height, 4)
        self.assertEqual(self.squa2.height, 5)

    def test_x(self):
        """ Testing for standard x """
        self.assertEqual(self.squa1.x, 0)
        self.assertEqual(self.squa2.x, 6)

    def test_y(self):
        """ Testing for standard y """
        self.assertEqual(self.squa1.y, 0)
        self.assertEqual(self.squa2.y, 0)

    def test_size_mandatory(self):
        """ Testing width mandatory """
        with self.assertRaises(TypeError):
            s = Square()

    def test_size_type(self):
        """ Testing non-ints for size """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("meh")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(None)

    def test_x_type(self):
        """ Testing non-ints for x """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(2, "hell")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(2, False)

    def test_y_type(self):
        """ Testing non-ints for y """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 2, "Pah!")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(3, 5, True)

    def test_size_value(self):
        """ Testing ints <= 0 for size """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(0)

    def test_x_value(self):
        """ Testing ints < 0 for x """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s = Square(3, -1)

    def test_y_value(self):
        """ Testing ints <= 0 for y """
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s = Square(1, 2, -1)

    def test_area(self):
        """ Testing area """
        self.assertEqual(self.squa1.area(), 16)
        self.assertEqual(self.squa2.area(), 25)

    def test_area_args(self):
        """ Testing too many args for area """
        with self.assertRaises(TypeError):
            a = self.squa1.area(4)

    def test_display_too_many_args(self):
        """ Testing display with too many args """
        with self.assertRaises(TypeError):
            self.squa1.display(9)
