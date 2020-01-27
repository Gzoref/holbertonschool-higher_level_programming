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
    
            
    def test_pep8(self):
        pep8_style = pep8.StyleGuide(quit=True)
        pep_check = pep8_style.check_files(['models/square.py'])
        self.assertEqual(pep_check.total_errors, 0, 'Pep8 Error in file')

    def test_area(self):
        r1 = Rectangle(3, 4)
        self.assertEqual(r1.area(), 12)
        