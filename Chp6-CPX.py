from adafruit_circuitplayground import cp
import time
import random

#Pattern for the neopixels
pattern = [0, 5, 2, 8, 1, 7, 3, 9, 4, 6]

#Random Color variations
def pixel_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

#Runs all the other programs
def main():
    while True:
        for pixel in pattern:
            cp.pixels[pixel] = pixel_color()
            time.sleep(0.5)
            cp.pixels[pixel] = (0, 0, 0)

main()
