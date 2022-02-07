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

img = PIL.Image.open('your_image.jpg')

converter = ImageEnhance.Color(img)

img3 = converter.enhance(2)

plt.imshow(img3)
plt.show()
