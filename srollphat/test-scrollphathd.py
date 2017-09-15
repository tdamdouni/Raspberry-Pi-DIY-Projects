# http://forums.pimoroni.com/t/scroll-phat-hd-pixelation-problems/5899

import time
import scrollphathd
from scrollphathd.fonts import font5x7


def do_test(text):
    for bright in [0.1, 0.25, 0.4, 0.55, 0.7]:
        scrollphathd.clear()
        scrollphathd.write_string(text, font=font5x7, brightness=bright)
        scrollphathd.show()
        time.sleep(0.75)

for test in range(3):
    for chars in ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR' ,'STU',
                  'VWX' ,'YZ0', '123', '456', '789', '!#?', '<>*']:
        print chars        
        do_test(chars)