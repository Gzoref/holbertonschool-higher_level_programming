import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseClass(unittest.TestCase):
    
    @classmethod
    def setUp(self):
       Base.base_instance = 0
       pass
            
    @classmethod
    def tearDownClass(self):
        pass
    
    def test_is_private(self):
        '''
        Is nb_object private
        '''
        self.assertTrue(hasattr(Base, 'base_instance'), 0)
    
    def test_object_id(self):
        '''
        Does id accept params
        '''
        base_instance_1 = Base(12)
        base_instance_2 = Base()
        base_instance_3 = Base()
        self.assertEqual(base_instance_1.id, 12)
        self.assertEqual(base_instance_2.id, 1)
        self.assertEqual(base_instance_3.id, 2)



    if __name__ == '__main__':
        unittest.main()
        