#! /usr/bin/env python3
# -*- coding: utf-8 -*- 

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("your_image.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

av5 = cv2.blur(img,(10,10))

plt.gcf().set_size_inches(25,25)
plt.imshow(av5)
plt.show()
