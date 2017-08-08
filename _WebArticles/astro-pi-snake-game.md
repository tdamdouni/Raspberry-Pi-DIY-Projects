# Astro Pi Snake Game

_Captured: 2017-07-30 at 15:33 from [www.stuffaboutcode.com](http://www.stuffaboutcode.com/2015/06/astro-pi-snake-game.html?m=1)_

I recently made [Snake](https://en.wikipedia.org/wiki/Snake_\(video_game\)) for the [Astro Pi](http://www.astropi.org/), just for fun really, but I am putting it online as I would like to see what others can do with it - it is literally screaming out to be hacked and improved.

I've given some ideas and tips but there is much more than could be done.

Anyone budding coders up for the challenge?

I started with the code I originally wrote for [Minecraft - Snake](http://www.stuffaboutcode.com/2013/03/raspberry-pi-minecraft-snake.html) and made the changes so that rather than creating blocks in Minecraft it turned on leds and used the joystick to control the motion. I was also surprised by how much I improved the overall structure of the code, it wasn't poorly coded it was just a bit untidy.

To try it yourself, get the code from [github.com/martinohanlon/AstroPiSnake](https://github.com/martinohanlon/AstroPiSnake) and run it, by opening a terminal and using the commands:
    
    
    git clone https://github.com/martinohanlon/AstroPiSnake
    cd AstroPiSnake
    sudo python astropisnake.py

What else could you do? How would you improve it? Can you improve it?

These are some of the ideas I thought of:

  1. Introduce levels, the better the player does, the faster the snake should go. The speed of the snake is set by the sleep in the startGame() method.
  2. The original game had more than one apple. The apple property would have to be changed to a list and the move() method would have to check if one of many apples had been eaten.
  3. Power ups - special apples which appear for a short amount of time and if you eat them you can go across the screen i.e. exiting the screen on the left would make you appear on the right.

Let me know how you get on - perhaps they'll be a prize!

![](http://3.bp.blogspot.com/-CkJJlv7dld4/VYZ7HY-YJEI/AAAAAAAAM14/whJHgmj6xhk/s280/astropisnake.JPG)
