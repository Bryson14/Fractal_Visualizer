#!/bin/env python3

# Julia Set Visualizer

import sys
from tkinter import mainloop
from Config import FractalData
from ImagePainter import ImagePainter
from Gradient import Gradients


class Julia:
	def __init__(self, images, image):
		self.image = image
		grad = Gradients()
		self.gradients = grad.get_gradients()
		self.len_x_axis = self.len_y_axis = 1024
		self.image_painter = ImagePainter(self.len_x_axis, self.len_y_axis, self.gradients[0])
		self.creal = images[image]["creal"]
		self.cimag = images[image]["cimag"]
		self.iterations = images[image]["iterations"]
		self.minx = images[image]["centerX"] - images[image]["axisLength"] / 2.0
		self.miny = images[image]["centerY"] - images[image]["axisLength"] / 2.0
		self.maxx = images[image]["centerX"] + images[image]["axisLength"] / 2.0
		self.maxy = images[image]["centerY"] + images[image]["axisLength"] / 2.0
		self.pixel_size = abs(self.maxx - self.minx) / self.len_x_axis

	def get_color_from_gradient(self, z):
		c = complex(self.creal, self.cimag)
		for i in range(self.iterations):
			z = z * z + c  # Iteratively compute z1, z2, z3 ...
			if abs(z) > 2:
				return self.gradients[i]  # The sequence unbinds itself

		return self.gradients[self.iterations]  # the sequence never unbinds itself

	def make_picture(self):
		for row in range(self.len_y_axis, 0, -1):
			for column in range(self.len_x_axis):
				x = self.minx + column * self.pixel_size
				y = self.miny + row * self.pixel_size
				color = self.get_color_from_gradient(complex(x, y))
				self.image_painter.img.put(color, (column, self.len_y_axis - row))
			self.image_painter.window.update()

	def draw_julia(self):
		self.make_picture()
		self.image_painter.img.write(f"drawn_fractals\{self.image}.png")
		print(f"Wrote image drawn fractals\{self.image}.png")

		mainloop()

