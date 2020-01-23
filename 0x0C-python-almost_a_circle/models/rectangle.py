#!/usr/bin/python3
'''
Write the class Rectangle that
inherits from Base:
'''
from models.base import Base


class Rectangle(Base):
    '''
    Class Rectangle inherits from Base
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Constructor
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    @property
    def width(self):
        '''
        Width getter
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Width setter
        '''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be > than 0')
        self.__width = value
    
    @property
    def height(self):
        '''
        height getter
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        height setter
        '''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be > than 0')
        self.__height = value
        
    @property
    def x(self):
        '''
        x getter
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        x setter
        '''
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be > than 0')
        self.__x = value
        
    @property
    def y(self):
        '''
        y getter
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        y setter
        '''
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be > than 0')
        self.__y = value
        
        
    def area(self):
        '''
        Returns area
        '''
        return self.width * self.height
    
    def display(self):
        '''
        Prints Rectangle to 
        console with #
        '''
        for i in range(self.height):
            print('# ' * self.width)

    def __str__(self):
        return f'[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}'
        