import time
import board
import neopixel

#pixels = neopixel.NeoPixel(board.D21, 7)

pixel_pin = board.D21

num_pixels = 7

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.9, auto_write=False, pixel_order=ORDER
)

# pixels.fill((159, 226, 191))
# pixels.show()


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)
        
def startup():
    rainbow_cycle(0.003)  # rainbow cycle with 1ms delay per step
    time.sleep(1)
    
    pixels.fill((0, 0, 0))
    pixels.show()
    
pixels.fill((0, 0, 0))
pixels.show()
        
# while True:
#     # Comment this line out if you have RGBW/GRBW NeoPixels
#     pixels.fill((159, 226, 191))
#     # Uncomment this line if you have RGBW/GRBW NeoPixels
#     # pixels.fill((255, 0, 0, 0))
#     pixels.show()
#     time.sleep(1)
# 
#     rainbow_cycle(0.003)  # rainbow cycle with 1ms delay per step
#     time.sleep(1)
#     
#     pixels.fill((0, 0, 0))
#     pixels.show()
#     
#     time.sleep(100)
