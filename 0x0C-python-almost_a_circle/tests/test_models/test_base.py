import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import pep8

class TestBaseClass(unittest.TestCase):
    
    @classmethod
    def setUp(self):
       Base._Base__nb_objects = 0
       pass
            
    @classmethod
    def tearDownClass(self):
        pass
    
    def test_is_private(self):
        '''
        Is nb_object private
        '''
        self.assertTrue(hasattr(Base, '_Base__nb_objects'), 0)

    def test_pep8(self):
        pep8_style = pep8.StyleGuide(quit=True)
        pep_check = pep8_style.check_files(['models/base.py'])
        self.assertEqual(pep_check.total_errors, 0, 'Pep8 Error in file')

    def test_docstring(self):
        self.assertIsNotNone(Base.__doc__)

    def test_object_id(self):
        '''
        Does id accept params
        '''
        base_instance_1 = Base(12)
        base_instance_2 = Base()
        base_instance_3 = Base()
        base_instance_4 = Base()
        self.assertEqual(base_instance_1.id, 12)
        self.assertEqual(base_instance_2.id, 1)
        self.assertEqual(base_instance_3.id, 2)
        self.assertEqual(base_instance_4.id, 3)

    def test_is_none(self):
        obj = Base(None)
        self.assertEqual(obj.id, 1)
    
    

    if __name__ == '__main__':
         unittest.main()
        