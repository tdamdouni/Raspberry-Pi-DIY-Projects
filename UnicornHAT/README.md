UnicornHAT
==========

Code related to my Unicorn HAT tinkering

cheertree.py
------------
A CheerLights christmas tree on you UnicornHAT.  Operates in one of 3 modes
- 0 = All; the tree is a mosaic of the past colours
- 1 = Lights; the main part of the tree is green with 5 lights and the star controlled by #cheerlights
- 2 = Star; just the top pixel changes to the most recent

Note: modes 1 and 2 swaps the colour green for yellow otherwise you wouldn't see it!

wordclock.py
------------
Inspired by this article http://blog.atmel.com/2014/12/01/build-your-own-micro-word-clock-with-an-atmega328p/
Blogged here http://fortoffee.org.uk/2014/12/word-clock-with-a-unicorn/

Uses an overlay to display the time as words by lighting up the relevant letter combinations
