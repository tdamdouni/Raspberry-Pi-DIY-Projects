#!/usr/bin/python
'''*****************************************************************************************************************
    Raspberry Pi + Raspbian Weather Station
    By Uladzislau Bayouski
    https://www.linkedin.com/in/uladzislau-bayouski-a7474111b/
    
    Weather entities (temperature, humidity, pressure) package.
********************************************************************************************************************'''

from abc import ABCMeta, abstractmethod, abstractproperty

from config import Config
from visual_styles import ArrowStyle, NumericStyle, SquareStyle, VisualStyle

class CarouselContainer(object):
    """
    Base class for carousel like classes.
    
    These classes contain list of items, and iterate through them functionality.
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        # Index of current carousel item
        self.current_index = 0

    @abstractproperty
    def carousel_items(self):
        """Carousel items to iterate through."""
        pass
   
    @property
    def next_item(self):
        """
        Gets next item, and sets its index as current_index.
        
        If item is the last one returns the first item.
        """
        if self.current_index < len(self.carousel_items) - 1:
            self.current_index += 1
        else:
            self.current_index = 0
            
        return self.current_item

    @property
    def previous_item(self):
        """
        Gets previous item, and sets its index as current_index.
        
        If item is the first one returns the last item.
        """
        if self.current_index > 0:
            self.current_index -= 1
        else:
            self.current_index = len(self.carousel_items) - 1
            
        return self.current_item

    @property
    def current_item(self):
        """Returns current item."""
        return self.carousel_items[self.current_index]

class WeatherEntityType(object):
    """Enum object for weather enitites types."""
    HUMIDITY, PRESSURE, TEMPERATURE = range(3)

class WeatherEntity(CarouselContainer):
    """Base class for weather entities implementations."""
    __metaclass__ = ABCMeta

    def __init__(self):
        super(WeatherEntity, self).__init__()

        # Default set of visual styles for weather entity instance
        self._visual_styles = (
            NumericStyle(self.positive_color, self.negative_color),
            ArrowStyle(self.positive_color, self.negative_color),
            SquareStyle(self.positive_color, self.negative_color)
        )

    @abstractproperty
    def entity_messsage(self):
        """Message to show when switching to it."""
        pass

    @abstractproperty
    def positive_color(self):
        """Color to use for positive values."""
        pass

    @abstractproperty
    def negative_color(self):
        """Color to use for negative values."""
        pass

    @abstractproperty
    def entity_type(self):
        """Returns WeatherEntityType value."""
        pass

    @property
    def carousel_items(self):
        return self._visual_styles

    @property
    def current_style(self):
        """Current applied visual style."""
        return self.current_item

    def show_pixels(self, value):
        """Shows pixel for current entity and applied visual style."""
        return self.current_item.apply_style(value)

class HumidityEntity(WeatherEntity):
    """Humidity enity implementation."""

    def __init__(self):
        super(HumidityEntity, self).__init__()

    @property
    def entity_messsage(self):
        return 'Humidity'

    @property
    def positive_color(self):
        return Config.HUM_POSITIVE

    @property
    def negative_color(self):
        return Config.HUM_NEGATIVE

    @property
    def entity_type(self):
        return WeatherEntityType.HUMIDITY

    def show_pixels(self, value):
        # For square visual style we divide by 100 and multiply by 64 (8x8 screen resolution) 
        # because humidity value is in percent
        if self.current_style is SquareStyle:
            value = 64 * value / 100

        return super(HumidityEntity, self).show_pixels(value)

class PressureEntity(WeatherEntity):
    """Pressure enity implementation."""

    def __init__(self):
        super(PressureEntity, self).__init__()
    
    @property
    def entity_messsage(self):
        return 'Pressure'

    @property
    def positive_color(self):
        return Config.PRESS_POSITIVE

    @property
    def negative_color(self):
        return Config.PRESS_NEGATIVE

    @property
    def entity_type(self):
        return WeatherEntityType.PRESSURE

class TemperatureEntity(WeatherEntity):    
    """Temperature enity implementation."""

    def __init__(self):
        super(TemperatureEntity, self).__init__()
    
    @property
    def entity_messsage(self):
        return 'Temperature'

    @property
    def positive_color(self):
        return Config.TEMP_POSITIVE

    @property
    def negative_color(self):
        return Config.TEMP_NEGATIVE

    @property
    def entity_type(self):
        return WeatherEntityType.TEMPERATURE

# Predefined weather entities tuple
DEFAULT_WEATHER_ENTITIES = (TemperatureEntity(), HumidityEntity(), PressureEntity())
