#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import skimage
import skimage.feature
import skimage.viewer
import cv2
import numpy as np
import matplotlib.pyplot as plt
import PIL
from PIL import ImageEnhance

img = PIL.Image.open('the-good-the-bad-and-the-ugly_764d_1920x1080.jpg')

converter = ImageEnhance.Brightness(img)

img3 = converter.enhance(2)

plt.imshow(img3)
plt.show()
