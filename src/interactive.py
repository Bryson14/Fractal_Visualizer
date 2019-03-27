#!/bin/env python3

# Interactive Mandelbrot Set Escape Time Visualizer
#
# This program does not need to be refactored for the assignment.
# It is provided to help you better understand the Mandelbrot fractal.
import sys
from tkinter import Tk, Canvas, mainloop
from Config import FractalData
from ImagePainter import ImagePainter
from Gradient import Gradients


class Interactive:
	def __init__(self, images, image):
		grad = Gradients()
		self.gradients = grad.get_gradients()
		self.MAX_ITERATIONS = len(self.gradients)
		self.CELL_SIZE = 20
		self.images = images
		self.len_x_axis = self.len_y_axis = 640
		self.minx = self.images[image]['centerX'] - (self.images[image]['axisLen'] / 2.0)
		self.maxx = self.images[image]['centerX'] + (self.images[image]['axisLen'] / 2.0)
		self.miny = self.images[image]['centerY'] - (self.images[image]['axisLen'] / 2.0)
		self.maxy = self.images[image]['centerY'] + (self.images[image]['axisLen'] / 2.0)
		self.pixelsize = abs(self.maxx - self.minx) / self.len_x_axis
		self.image_painter = ImagePainter(self.len_x_axis, self.len_y_axis, self.gradients[-1])
		self.window = Tk()
		self.canvas = Canvas(self.window, width=self.len_x_axis, height=self.len_y_axis, bg=self.gradients[-1])

	def colorOfThePixel(self, c , verbose=False):
		"""Return the color of the current pixel within the Mandelbrot set"""
		self.z = complex(0, 0)  # z0
		
		for i in range(self.MAX_ITERATIONS):
			self.z = self.z * self.z + c  # Get z1, z2, ...
			if verbose:
				print(f"i={i+1}, Z={self.z}")
			if abs(self.z) > 2:
				if verbose:
					print(f"Escaped on iteration #{i+1}! abs(Z)={abs(self.z)}\n")
				return i  # The sequence is unbounded
		if verbose:
			print(f"No escape after {self.MAX_ITERATIONS} iterations, I give up\n")
		return self.MAX_ITERATIONS - 1   # Indicate a bounded sequence

	def paintCell(self, event):
		col = (event.x // self.CELL_SIZE) * self.CELL_SIZE
		row = self.len_x_axis - ((event.y // self.CELL_SIZE) * self.CELL_SIZE)
		x = self.minx + col * self.pixelsize
		y = self.miny + row * self.pixelsize
		count = self.colorOfThePixel(complex(x, y), verbose=True)
		color = self.gradients[count]
		canvas = event.widget
		canvas.create_rectangle(col, self.len_x_axis-row, col+self.CELL_SIZE, self.len_x_axis-row+self.CELL_SIZE, fill=color)

	def paintEntireImage(self, event):
		"""Paint the entire image"""

		for row in range(self.len_x_axis, -1, -self.CELL_SIZE):
			for col in range(self.len_y_axis, -1, -self.CELL_SIZE):
				x = self.minx + col * self.pixelsize
				y = self.miny + row * self.pixelsize
				count = self.colorOfThePixel(complex(x, y))
				color = self.gradients[count]
				self.image_painter.canvas.create_rectangle(col, self.len_x_axis-row, col+self.CELL_SIZE, self.len_y_axis-row+self.CELL_SIZE, fill=color)

	def draw(self):
		self.image_painter.canvas.pack()
		self.image_painter.canvas.bind("<Button-1>", self.paintCell)
		self.image_painter.canvas.bind("<Button-3>", self.paintEntireImage)
		self.image_painter.window.bind("<space>", self.paintEntireImage)
		mainloop()


def main():
	mandels = FractalData()
	images = mandels.get_mandelbrot_dic()

	if len(sys.argv) < 2:
		print("Usage: interactive.py FRACTALNAME")
		print("Where FRACTALNAME is one of:")
		for image in images:
			print(f"\t{image}")
		sys.exit(1)

	elif str(sys.argv[1]).lower() not in images:
		print(f"ERROR: {sys.argv[1]} is not a valid fractal")
		print("Please choose one of the following:")
		for i in images:
			print(f"\t{i}")
		sys.exit(1)

	else:
		image = str(sys.argv[1]).lower()

	interactive_fractal = Interactive(images, image)
	interactive_fractal.draw()


if __name__ == '__main__':
	main()
