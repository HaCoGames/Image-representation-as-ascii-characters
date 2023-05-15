import cv2
import numpy as np
import os


ASCII_CHARS = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. """[::-1]
ASCII_CHARS_LENGTH = len(ASCII_CHARS)

def main():
    path_to_image = input('Enter path to image: ')
    image = cv2.imread(path_to_image)

    # convert to grayscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # normalize image
    image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)

    # get terminal sizes:
    rows = os.get_terminal_size().lines
    cols = int((rows/9) * 16)

    print (cols, rows)

    image = cv2.resize(image, (rows, cols))

    for r in range(rows):
        for c in range(cols):
            # get pixel at position (c, r)
            pixel = image[c, r]
            
            print(ASCII_CHARS[int(pixel/ASCII_CHARS_LENGTH)], end='')
        print()

main()