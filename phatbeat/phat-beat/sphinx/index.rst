.. role:: python(code)
   :language: python

.. toctree::
   :titlesonly:
   :maxdepth: 0

Welcome
-------

This documentation will guide you through the methods available in the pHAT BEAT python library.

* More information - https://shop.pimoroni.com/products/phat-beat
* Get the code - https://github.com/pimoroni/phat-beat
* Get help - http://forums.pimoroni.com/c/support

At A Glance
-----------

.. automoduleoutline:: phatbeat
   :members:

Handle A Button Press
---------------------

To handle a button press, you should use the :python:`on` method as a decorator, like so::

    @phatbeat.on(phatbeat.BTN_FASTFWD)
    def fastfwd(pin):
        print("Fast Forward Pressed")


.. automodule:: phatbeat
   :noindex:
   :members: on

Set A Single Pixel
------------------

To control the dual VU meters on your pHAT BEAT manually you need to tell each pixel what colour to be. This is done via set_pixel.

The :python:`brightness` argument is completely optional. Omit it to keep the last
brightness value set for that particular pixel.

If :python:`channel` is specified then you can set pixels 0-7 on the given channel (0-1). Otherwise it treats the pixels as one chain of 16 (0-15).

.. automodule:: phatbeat
   :noindex:
   :members: set_pixel

Set All Pixels
--------------

Sometimes you need to set all the pixels to the same colour. This convinience method does just that!

To set just one channel or the other, specify channel 0 or 1.

.. automodule:: phatbeat
   :noindex:
   :members: set_all

Show
----

None of your pixels will appear until you :python:`show()` them. This method writes
all the pixel data out to your device.

.. automodule:: phatbeat
   :noindex:
   :members: show

Clear
-----

Exactly the same as calling :python:`set_all(0,0,0)`, clear sets all the pixels to black.

You must also call :python:`show()` if you want to turn the displays off.

.. automodule:: phatbeat
   :noindex:
   :members: clear

Enable/Disable Clear On Exit
----------------------------

Sometimes you want a script that runs and quits, leaving a pattern up on the displays.


.. automodule:: phatbeat
   :noindex:
   :members: set_clear_on_exit

Constants
---------

The following constants denote available buttons for pHAT BEAT.

* :python:`BTN_FASTFWD = 5`
* :python:`BTN_REWIND = 13`
* :python:`BTN_PLAYPAUSE = 6`
* :python:`BTN_VOLUP = 16`
* :python:`BTN_VOLDN = 26`
* :python:`BTN_ONOFF = 12`
* :python:`BUTTONS` list of all available buttons

