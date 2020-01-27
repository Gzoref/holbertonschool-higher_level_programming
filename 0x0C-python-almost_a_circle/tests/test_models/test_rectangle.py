import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8
import json

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
        self.assertTrue(str(Rectangle), "<class 'models.rectangle.Rectangle'>")
        
    def test_pep8(self):
        '''
        Test pep8
        '''
        pep8_style = pep8.StyleGuide(quit=True)
        pep_check = pep8_style.check_files(['models/rectangle.py'])
        self.assertEqual(pep_check.total_errors, 0, 'Pep8 Error in file')
        
    def test_B_inheritance(self):
        '''
        Tests if Rectangle inherits Base.
        '''
        self.assertTrue(issubclass(Rectangle, Base))
    
    def test_id(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r2.id, 12)