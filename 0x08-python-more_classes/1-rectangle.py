#!/usr/bin/python3
"""
The properties and dimesions of rectangel
"""

class Rectangle:
    """
    class of rectangle give the propertise of the rectangle

    Attributes:
        width (int): width of rectangle
        height (int): height of rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Creates new instances of Rectangel

        Args:
        width (int, optional): width of rectangle. Defaults to 0
        height (int, optional): height of rectangle.  Defaults to 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Width retriver.

        Returns:
            int: the width of rectangle
        """
        return self.width

    @property
    def height(self):
        """
        height retriver
        
        Returns:
        int: the height of rectangle
        """
        return self.height

    @width.setter
    def width(self, value):
         """Property setter for width of rectangle.

        Args:
            value (int): width of the rectangle.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
          """Property setter for height of recyangle.

        Args:
            value (int): height of the rectangle.

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
