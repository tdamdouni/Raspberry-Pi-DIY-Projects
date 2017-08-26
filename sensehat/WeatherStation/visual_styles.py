'''*****************************************************************************************************************
    Raspberry Pi + Raspbian Weather Station
    By Uladzislau Bayouski
    https://www.linkedin.com/in/uladzislau-bayouski-a7474111b/
    
    Visual styles package.
********************************************************************************************************************'''
    
from abc import ABCMeta, abstractmethod, abstractproperty

class VisualStyle(object):
    """Base class for all visual styles."""
    __metaclass__ = ABCMeta

    def __init__(self, positive_color, negative_color):
        # No color for led
        self._e = (0, 0, 0) 

        # We use positive and negative color tuples to figure out the color applied to visual style
        # For example:
        #   +23 Celsius is shown as 23 in red color
        #   -15 Celsius is shown as 15 in blue color
        self._p = positive_color
        self._n = negative_color

    @property
    def rotation(self):
        """Rotation to be applied to a pixel map."""
        return 0

    @abstractmethod
    def apply_style(self, value):
        """Applies style for given value."""
        pass

class ArrowStyle(VisualStyle):
    """
    Arrow visual style implementation.
    
    Depends on previous and new values:
        a) if new/current value is bigger than previous shows arrow up
        b) if new/current values is less than previous shows arrow down
        c) if values are equal shows equals symbol
    """

    def __init__(self, positive_color, negative_color):
        super(ArrowStyle, self).__init__(positive_color, negative_color)

        # Previous value to be used for style render
        self._previous_value = 0

        # Arrow up pixels map
        self._arrow_up = (
            self._e, self._e, self._e, self._p, self._p, self._e, self._e, self._e, #0
            self._e, self._e, self._p, self._p, self._p, self._p, self._e, self._e, #1
            self._e, self._p, self._e, self._p, self._p, self._e, self._p, self._e, #2
            self._p, self._e, self._e, self._p, self._p, self._e, self._e, self._p, #3
            self._e, self._e, self._e, self._p, self._p, self._e, self._e, self._e, #4
            self._e, self._e, self._e, self._p, self._p, self._e, self._e, self._e, #5
            self._e, self._e, self._e, self._p, self._p, self._e, self._e, self._e, #6
            self._e, self._e, self._e, self._p, self._p, self._e, self._e, self._e  #7
        )

        # Arrow down pixels map
        self._arrow_down = tuple(self._n if pixel is self._p else self._e for pixel in self._arrow_up[::-1])

        # Equals symbol pixels map
        self._equals = (
            self._e, self._e, self._e, self._e, self._e, self._e, self._e, self._e, #0
            self._e, self._e, self._e, self._e, self._e, self._e, self._e, self._e, #1
            self._p, self._p, self._p, self._p, self._p, self._p, self._p, self._p, #2
            self._p, self._p, self._p, self._p, self._p, self._p, self._p, self._p, #3
            self._n, self._n, self._n, self._n, self._n, self._n, self._n, self._n, #4
            self._n, self._n, self._n, self._n, self._n, self._n, self._n, self._n, #5
            self._e, self._e, self._e, self._e, self._e, self._e, self._e, self._e, #6
            self._e, self._e, self._e, self._e, self._e, self._e, self._e, self._e, #7
        )
    
    def apply_style(self, value):
        # Need delta of current and previous values to figure what symbol to show
        new_value = value
        new_value -= self._previous_value
        self._previous_value = value

        # If no changes, show equals symbol
        if not new_value:
            return self._equals

        return self._arrow_up if new_value > 0 else self._arrow_down

class NumericStyle(VisualStyle):
    """
    Numeric visual style implementation.
    
    Shows one/two digits values.
    In case value has more than 2 digits shows infinity symbol.
    """
    
    def __init__(self, positive_color, negative_color):
        super(NumericStyle, self).__init__(positive_color, negative_color)

        # Empty line, used to build final number
        self._empty_line = (self._e, self._e, self._e, self._e, self._e, self._e, self._e, self._e)
        
        # Numbers dictionary: key is number as string, value is its pixel map
        self._numbers = {
            '0': (
                self._p, self._p, self._p, self._p, self._p, self._p, self._p, self._p,
                self._p, self._e, self._e, self._e, self._e, self._e, self._e, self._p,
                self._p, self._p, self._p, self._p, self._p, self._p, self._p, self._p,
            ),
            '1': (
                self._p, self._p, self._p, self._p, self._p, self._p, self._p, self._p,
                self._e, self._p, self._e, self._e, self._e, self._e, self._e, self._e,
                self._e, self._e, self._p, self._e, self._e, self._e, self._e, self._e,
            ),
            '2': (
                self._p, self._p, self._p, self._p, self._p, self._e, self._e, self._p,
                self._p, self._e, self._e, self._e, self._p, self._e, self._e, self._p,
                self._p, self._e, self._e, self._e, self._p, self._p, self._p, self._p,
            ),
            '3': (
                self._p, self._p, self._p, self._p, self._p, self._p, self._p, self._p,
                self._p, self._e, self._e, self._e, self._p, self._e, self._e, self._p,
                self._p, self._e, self._e, self._e, self._p, self._e, self._e, self._p,
            ),
            '4': (
                self._p, self._p, self._p, self._p, self._p, self._p, self._p, self._p,
                self._e, self._e, self._e, self._e, self._p, self._e, self._e, self._e,
                self._p, self._p, self._p, self._p, self._p, self._e, self._e, self._e,
            ),
            '5': (
                self._p, self._e, self._e, self._e, self._p, self._p, self._p, self._p,
                self._p, self._e, self._e, self._e, self._p, self._e, self._e, self._p,
                self._p, self._p, self._p, self._p, self._p, self._e, self._e, self._p,
            ),
            '6': (
                self._p, self._e, self._e, self._e, self._p, self._p, self._p, self._p,
                self._p, self._e, self._e, self._e, self._p, self._e, self._e, self._p,
                self._p, self._p, self._p, self._p, self._p, self._p, self._p, self._p,
            ),
            '7': (
                self._p, self._p, self._p, self._p, self._p, self._p, self._p, self._p,
                self._p, self._e, self._e, self._e, self._e, self._e, self._e, self._e,
                self._p, self._e, self._e, self._e, self._e, self._e, self._e, self._e,
            ),
            '8': (
                self._p, self._p, self._p, self._p, self._p, self._p, self._p, self._p,
                self._p, self._e, self._e, self._e, self._p, self._e, self._e, self._p,
                self._p, self._p, self._p, self._p, self._p, self._p, self._p, self._p,
            ),
            '9': (
                self._p, self._p, self._p, self._p, self._p, self._p, self._p, self._p,
                self._p, self._e, self._e, self._e, self._p, self._e, self._e, self._p,
                self._p, self._p, self._p, self._p, self._p, self._e, self._e, self._p,
            )
        }

        # Infinity symbol used for bigger than 2 digits numbers
        self._infinity = (
            self._e, self._e, self._e, self._p, self._p, self._e, self._e, self._e,
            self._e, self._e, self._p, self._e, self._e, self._p, self._e, self._e,
            self._e, self._e, self._p, self._e, self._e, self._p, self._e, self._e,
            self._e, self._e, self._e, self._p, self._p, self._e, self._e, self._e,
            self._e, self._e, self._e, self._p, self._p, self._e, self._e, self._e,
            self._e, self._e, self._p, self._e, self._e, self._p, self._e, self._e,
            self._e, self._e, self._p, self._e, self._e, self._p, self._e, self._e,
            self._e, self._e, self._e, self._p, self._p, self._e, self._e, self._e,
        )

    @property
    def rotation(self):
        # We need to rotate due to specific way of building number pixel map
        return 90

    def apply_style(self, value):
        # We need to get abs as we do not show minus symbol, we use different colors for this
        # We need to round value, we show only 2 digits and 25.8 is closer to 26 from UX perspecrtive
        # We call int to make sure we use integer rather than float
        # We call str to convert 2 digits number to string for futher parsing
        str_value = str(int(round(abs(value))))

        # If number is 2 digits build 2 digits pixel map
        if len(str_value) == 2:
            result = list(self._numbers[str_value[1]]) #0-2
            result += self._empty_line * 2             #3-4
            result += self._numbers[str_value[0]]      #5-7
        # If number is one digit show one digit pixel map
        elif len(str_value) == 1:
            result = list(self._empty_line * 2)        #0-1
            result += self._numbers[str_value]         #2-4
            result += self._empty_line * 3             #5-7
        # Or show infinity symbol
        else:
            result = self._infinity

        # Figure out what color to use depending on positive or negative value
        if value <= 0:
            result = tuple(self._n if pixel is self._p else self._e for pixel in result)

        return result
            

class SquareStyle(VisualStyle):
    """
    Square visual style implementation.
    
    Visualize value as a square of different colored pixels.
    """
    
    def __init__(self, positive_color, negative_color):
        super(SquareStyle, self).__init__(positive_color, negative_color)

    def apply_style(self, value):
        # Depending on value we use positive or negative color to fill pixels.
        # We use range of 64 because the screen resolution is 8x8
        if value > 0:
            return tuple(self._p if i < value else self._n for i in range(64))

        return tuple(self._n if i < -value else self._p for i in range(64))
