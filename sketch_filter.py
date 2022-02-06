#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

class Sketcher(object):

	def __init__(self):
		pass

	def resize(self,image,window_height = 500):
		aspect_ratio = float(image.shape[1])/float(image.shape[0])
		window_width = window_height/aspect_ratio
		image = cv2.resize(image, (int(window_height),int(window_width)))
		return image	
	
	def render(self, img_rgb):
		img_rgb = cv2.imread(img_rgb)
		img_rgb = self.resize(img_rgb, 500)
		numDownSamples = 2
		numBilateralFilters = 50

		img_color = img_rgb
		for _ in range(numDownSamples):
			img_color = cv2.pyrDown(img_color)

		for _ in range(numBilateralFilters):
			img_color = cv2.bilateralFilter(img_color, 9, 9, 7)
		
		for _ in range(numDownSamples):
			img_color = cv2.pyrUp(img_color)
	
		img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
		img_blur = cv2.medianBlur(img_gray, 3)

		img_edge = cv2.adaptiveThreshold(img_blur, 255,
										 cv2.ADAPTIVE_THRESH_MEAN_C,
										 cv2.THRESH_BINARY,9, 2)

		(x,y,z) = img_color.shape
		img_edge = cv2.resize(img_edge,(y,x))
		img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)

		return img_edge

	def start(self, img_path):
		tmp_canvas = Sketcher()
		file_name = img_path
		res = tmp_canvas.render(file_name)
		cv2.imwrite("Sketch version.jpg", res)
		cv2.imshow("Sketch version", res)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		print("Image saved as 'Sketch version.jpg'")
	
img = Sketcher()

img.start('the-good-the-bad-and-the-ugly_764d_1920x1080.jpg')
