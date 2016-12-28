__author__ = 'eguoshi'

'''
Create Thumbnails
'''

import os
from PIL import Image

SIZE = (75, 75)
SAVE_DIRECTORY = 'thumbs'

def get_image_paths(folder):
    return (os.path.join(folder, f)
            for f in os.listdir(folder)
            if 'jpg' in f)


def create_thubnail(filename):
    im = Image.open(filename)
    im.thumbnail(SIZE, Image.ANTIALIAS)
    base, fname = os.path.split(filename)

    save_path = os.path.join(base, SAVE_DIRECTORY, fname)
    im.save(save_path)


if __name__ == '__main__':
    folder = os.path.abspath('C:\Users\Public\Pictures\Sample Pictures')
    os.mkdir(os.path.join(folder, SAVE_DIRECTORY))

    images = get_image_paths(folder)

    for image in images:
        create_thubnail(image)