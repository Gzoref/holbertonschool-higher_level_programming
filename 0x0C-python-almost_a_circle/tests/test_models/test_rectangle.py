import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangleClass(unittest.TestCase):
    
    @classmethod
    def setUp(self):
       Base.base_instance = 0
       pass
            
    @classmethod
    def tearDownClass(self):
        pass
    
    def test_class(self):
        '''
        Rectangle is a class
        '''
        self.assertTrue(str(Rectangle), "<class 'models.rectangle.Rectangle'>")
        
    def test_B_inheritance(self):
        '''Tests if Rectangle inherits Base.'''
        self.assertTrue(issubclass(Rectangle, Base))
    
    if __name__ == '__main__':
        unittest.main()