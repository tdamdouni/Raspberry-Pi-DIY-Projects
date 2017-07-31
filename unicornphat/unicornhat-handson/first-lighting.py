# set up unicorn pHAT
import unicornhat as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
# unicorn.brightness(0.5)
unicorn.brightness(1.0)

unicorn.set_pixel(0, 1, 255, 0, 0)
unicorn.show()
