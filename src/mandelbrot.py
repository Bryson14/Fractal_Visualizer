#!/bin/env python3

# Mandelbrot Set Visualizer

from tkinter import mainloop
from ImagePainter import ImagePainter
from Gradient import Gradients


class Mandelbrot:
	def __init__(self, images, image):
		grad = Gradients()
		self.gradients = grad.get_gradients()
		self.images = images
		self.image = image
		self.len_x_axis = self.len_y_axis = 640
		self.minx = images[image]['centerX'] - (images[image]['axisLen'] / 2.0)
		self.maxx = images[image]['centerX'] + (images[image]['axisLen'] / 2.0)
		self.miny = images[image]['centerY'] - (images[image]['axisLen'] / 2.0)
		self.maxy = images[image]['centerY'] + (images[image]['axisLen'] / 2.0)
		self.pixelsize = abs(self.maxx - self.minx) / self.len_x_axis
		self.image_painter = ImagePainter(self.len_x_axis, self.len_y_axis+, self.gradients[0])

	def iteration_exit_count(self, c):
		"""Return the color of the current pixel within the Mandelbrot set"""
		z = complex(0, 0)  #z0
		for i in range(len(self.gradients)):
			z = z * z + c  # Get z1, z2, ...
			if abs(z) > 2:
				return i  # The sequence is unbounded

		return (self.gradients) - 1   # Indicate a bounded sequence

	def paint(self):
		for row in range(self.len_x_axis, 0, -1):
			for col in range(self.len_y_axis):
				x = self.minx + col * self.pixelsize
				y = self.miny + row * self.pixelsize
				exit_count = self.iteration_exit_count(complex(x, y))
				color = self.gradients[exit_count]
				self.image_painter.img.put(color, (col, self.len_x_axis - row))
			self.image_painter.window.update()

	def draw_mandelbrot(self):
		self.paint()
		self.image_painter.img.write(f"drawn_fractals\{self.image}.png")
		print(f"Wrote image drawn fractals\{self.image}.png")
		mainloop()
