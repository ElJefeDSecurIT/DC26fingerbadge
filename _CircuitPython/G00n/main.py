# CircuitPython demo - NeoPixel

import time
import board
import neopixel


# On CircuitPlayground Express -> Board.NEOPIXEL
# Otherwise choose an open pin connected to the Data In of the NeoPixel strip,
# such as board.D1
# pylint: disable=no-member
pin = board.D1

# The number of pixels in the strip
pix = 3

# number of colors in each pixel, =3 for RGB, =4 for RGB plus white
BPP = 3

strip = neopixel.NeoPixel(pin, pix, bpp=BPP, brightness=0.3, auto_write=True)

def format_tuple(r, g, b):
    if BPP == 3:
        return (r, g, b)
    return (r, g, b, 0)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0) or (pos > 255):
        return format_tuple(0, 0, 0)
    if pos < 85:
        return format_tuple(int(pos * 3), int(255 - (pos*3)), 0)
    if pos < 170:
        pos -= 85
        return format_tuple(int(255 - pos*3), 0, int(pos*3))
    pos -= 170
    return format_tuple(0, int(pos*3), int(1 - pos*3))

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(strip.n):
            idx = int((i * 256 / len(strip)) + j)
            strip[i] = wheel(idx & 255)
        strip.show()
        time.sleep(wait)

while True:
#cycle Red
    for z in range(132):
        strip.fill(format_tuple(0, z, 0))
        strip.show()
#    time.sleep(1)
    
    i = 132
    while i:
        strip.fill(format_tuple(0, i, 0))
        strip.show()
        i = i-1
    time.sleep(.69)

#cycle Blue


#    for z in range(128):
#        strip.fill(format_tuple(0, 0, z))
#        strip.show()
#    time.sleep(1)
  
#    i = 128
#    while i:
#        strip.fill(format_tuple(0, 0, i))
#        strip.show()
#        i = i-1
#    time.sleep(1)
    
#    strip.fill(format_tuple(255, 0, 255))
#    strip.show()
#    time.sleep(1)
#    rainbow_cycle(0.0001)    # rainbowcycle with 1ms delay per step