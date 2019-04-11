#!/bin/env python3

from tkinter import mainloop
from fractal import Fractal


class Mandelbrot(Fractal):
	def __init__(self, image, colors):
		super().__init__(image, colors)
		self.len_x_axis = self.len_y_axis = 640

	def count(self, c):
		z = complex(0, 0)
		for i in range(len(self.gradients)):
			z = z * z + c
			if abs(z) > 2:
				return i
		return len(self.gradients) - 1

	def paint(self):
		for row in range(self.len_x_axis, 0, -1):
			for col in range(self.len_y_axis):
				x = self.minx + col * self.pixel_size
				y = self.miny + row * self.pixel_size
				exit_count = self.count(complex(x, y))
				self.image_painter.img.put(self.gradients[exit_count], (col, self.len_x_axis - row))
			self.image_painter.window.update()

	def draw(self):
		self.paint()
		self.image_painter.img.write(f"drawn_fractals\{self.image['name']}.png")
		print(f"Wrote image drawn fractals\{self.image['name']}.png")
		mainloop()
