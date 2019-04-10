#!/bin/env python3

from tkinter import mainloop
from fractal import Fractal


class Burningship(Fractal):
	def __init__(self, images, image, colors):
		Fractal.__init__(images, image, colors)
		self.len_x_axis = self.len_y_axis = 620
		self.creal = images[image]["creal"]
		self.cimag = images[image]["cimag"]
		self.iterations = images[image]["iterations"]

	def count(self, z):
		c = complex(self.creal, self.cimag)
		for i in range(self.iterations):
			z = z * z + c
			if abs(z) > 2:
				return i
		return self.iterations

	def paint(self):
		for row in range(self.len_y_axis, 0, -1):
			for column in range(self.len_x_axis):
				x = self.minx + column * self.pixel_size
				y = self.miny + row * self.pixel_size
				exit_count = self.count(complex(x, y))
				self.image_painter.img.put(self.gradients[exit_count], (column, self.len_y_axis - row))
			self.image_painter.window.update()

	def draw(self):
		self.paint()
		self.image_painter.img.write(f"drawn_fractals\{self.image}.png")
		print(f"Wrote image:  drawn_fractals\{self.image}.png")

		mainloop()

