import cv2
import numpy as np
import os
import urllib.request

from sys import argv

ASCII_CHARS = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. """[::-1]
ASCII_CHARS_LENGTH = len(ASCII_CHARS)

def main():
    if len(argv) == 1:
        path_to_image = input('Enter path to image: ')
    else:
        path_to_image = argv[1]

    if not os.path.isfile(path_to_image):
        req = urllib.request.urlopen(path_to_image)
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        image = cv2.imdecode(arr, -1)
    else:
        image = cv2.imread(path_to_image)

    # convert to grayscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # normalize image
    image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)

    cv2.imshow('image', image)
    cv2.waitKey(0)

    # rotate image
    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    image = cv2.flip(image, 1)

    # get normal image size:
    height_n, width_n = image.shape

    height = os.get_terminal_size().lines
    width = int((height*width_n)/height_n)

    if width > os.get_terminal_size().columns:
        width = os.get_terminal_size().columns
        height = int((width*height_n)/width_n)

    print (f"Width: {width}", f"Height: {height}")

    image = cv2.resize(image, (height, width))

    for r in range(height):
        for c in range(width):
            # get pixel at position (c, r)  
            pixel = image[c, r]
            char_index = 0

            char_index = int((pixel/255) * (ASCII_CHARS_LENGTH-1))
            
            print(ASCII_CHARS[char_index], end='')
        print()

main()