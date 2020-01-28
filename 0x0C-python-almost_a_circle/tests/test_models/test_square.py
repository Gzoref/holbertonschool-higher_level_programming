import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import pep8

class TestRectangleClass(unittest.TestCase):

    @classmethod
    def setUp(self):
        pass            
    
    @classmethod
    def tearDownClass(self):
        pass
    
    def test_class(self):
        '''
        Rectangle is a class
        '''
        self.assertTrue(str(Square), "<class 'models.square.Square'>")
        
        
    def test_B_inheritance(self):
        '''Tests if Rectangle inherits Base.'''
        self.assertTrue(issubclass(Square, Base))

    def test_area(self):
        r1 = Rectangle(3, 4)
        self.assertEqual(r1.area(), 12)
        