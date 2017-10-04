# Raspberry Pi Physical Dashboard Configuration Parsing
# Author: Tony DiCola
#
# The MIT License (MIT)
#
# Copyright (c) 2016 Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from ConfigParser import SafeConfigParser

import widget


class Config(object):
    """Class to load and process dashboard configuration file data."""

    def __init__(self, filename):
        """Create an instance of the configuration by loading data from the
        provided config filename.
        """
        # Load the configuration.
        self._parser = SafeConfigParser()
        if len(self._parser.read(filename)) == 0:
            # Failed to load the config file, throw an error.
            raise RuntimeError('Failed to find configuration file with name: {0}'.format(filename))

    def get_widgets(self):
        """Return a dict of widget instances defined in the configuration file.
        The key of the dict is the widget instance name (as defined by the config
        section value) and the dict value is the widget class instance.
        """
        widgets = {}
        # Go through each section of the configuration and attempt to load each
        # widget as specifed by their type.
        for section in self._parser.sections():
            # Skip this section if it has no type option (i.e. isn't a widget).
            if not self._parser.has_option(section, 'type'):
                continue
            # Grab the type and find the associated widget type.
            type_name = self._parser.get(section, 'type')
            widget_class = widget.find_widget(type_name)
            if widget_class is None:
                print('Ignored configuration for widget "{0}" with unknown type: {1}'.format(section, type_name))
                continue
            print('Loading widget: {0}'.format(section))
            # Create the widget and add it to the list of known widgets.
            params = dict(self._parser.items(section))
            del params['type']   # Remove type attribute since it's not used by
                                 # widget constructors.
            try:
                # Call the widget constructor and pass in all the options in
                # the section, then store the created widget in the results.
                widgets[section.lower()] = widget_class(**params)
            except IOError as ex:
                raise RuntimeError('Failed to find widget "{0}" on I2C bus!  Make sure device is wired correctly and powered up.'.format(section))
        return widgets
