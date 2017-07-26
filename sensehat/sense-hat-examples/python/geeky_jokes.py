from sense_hat import SenseHat
from pyjokes import get_joke

sense = SenseHat()

joke = get_joke()

sense.show_message(joke)
