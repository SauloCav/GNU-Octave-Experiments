#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

def findMax(k):
	mx = 0
	for i in k:
		if i>mx:
			mx = i
	return mx

class Negative(object):

	def __init__(self):
		pass

	def resize(self,image,window_height = 500):
		aspect_ratio = float(image.shape[1])/float(image.shape[0])
		window_width = window_height/aspect_ratio
		image = cv2.resize(image, (int(window_height),int(window_width)))
		return image	
	
	def render(self, img_rgb):
		img_gray = cv2.imread(img_rgb, 0)
		img_gray = self.resize(img_gray, 500)

		k = []
		for i in range(img_gray.shape[0]):
			for j in range(img_gray.shape[1]):
				k.append(img_gray[i,j])

		L = findMax(k)
		dst = img_gray[:]

		for i in range(img_gray.shape[0]):
			for j in range(img_gray.shape[1]):
				dst[i,j] = L - dst[i,j]
		return dst

	def start(self, img_path):
		tmp_canvas = Negative()
		file_name = img_path
		res = tmp_canvas.render(file_name)
		cv2.imwrite("Negative_version.jpg", res)
		cv2.imshow("Negative Version", res)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		print("Image saved as 'Negative_version.jpg'")
	
img = Negative()

img.start('the-good-the-bad-and-the-ugly_764d_1920x1080.jpg')
