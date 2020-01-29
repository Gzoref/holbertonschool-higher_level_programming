import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8
import json


class TestRectangleClass(unittest.TestCase):

    @classmethod
    def setUp(cls):
        Base._Base__nb_objects = 0
        cls.rect1 = Rectangle(2, 4)
        cls.rect2 = Rectangle(2, 4, 6)
        cls.rect2 = Rectangle(2, 4, 6, 8)
        cls.rect2 = Rectangle(2, 4, 6, 8, 10)

    @classmethod
    def tearDownClass(self):
        pass

    def test_class(self):
        '''
        Rectangle is a class
        '''
        self.assertTrue(str(Rectangle), "<class 'models.rectangle.Rectangle'>")

    def test_B_inheritance(self):
        '''
        Tests if Rectangle inherits Base.
        '''
        self.assertTrue(issubclass(Rectangle, Base))

    def test_id_4(self):
        b1 = Base(1)
        b2 = Base(2)
        b3 = Base(3)
        b4 = Base(69)
        b5 = Base(4)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 69)
        self.assertEqual(b5.id, 4)

    def test_id(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 4)
        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r2.id, 12)

    def test_to_dict(self):
        dict1 = self.rect1.to_dictionary()
        self.assertEqual(
            {'x': 0, 'y': 0, 'id': 1, 'height': 4, 'width': 2}, dict1)

    def test_area(self):
        r1 = Rectangle(10, 10, 10, 10, 42)
        self.assertEqual(str(r1), '[Rectangle] (42) 10/10 - 10/10')

    def test_update(self):
        rect1 = {'id': 42, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        rect2 = {'id': 23, 'width': 4, 'height': 3, 'x': 5, 'y': 12}
        rdct_create1 = Rectangle.create(**rect1)
        rdct_create2 = Rectangle.create(**rect2)
        self.assertEqual('[Rectangle] (42) 3/4 - 1/2', str(rdct_create1))
        self.assertEqual('[Rectangle] (23) 5/12 - 4/3', str(rdct_create2))
        self.assertTrue(isinstance(rect1, dict))
        self.assertTrue(isinstance(rect2, dict))

    def test_save_to_file(self):
        Rectangle.save_to_file(None)
        with open('Rectangle.json', 'r') as f:
            self.assertEqual('[]', f.read())

    def test_save_load_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        load_file = Rectangle.load_from_file()
        self.assertTrue(isinstance(load_file, list))

    def test_args(self):
        with self.assertRaises(TypeError):
            rect1 = Rectangle()
            self.rect1.area(1)
