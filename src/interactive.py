#!/bin/env python3

# Interactive Mandelbrot Set Escape Time Visualizer
#
# This program does not need to be refactored for the assignment.
# It is provided to help you better understand the Mandelbrot fractal.
import sys
from tkinter import Tk, Canvas, PhotoImage, mainloop
from fractal_data import FractalData


class Interactive:
	def __init__(self, images, image):
		self.gradients = [
			'#ffe4b5', '#ffe5b2', '#ffe7ae', '#ffe9ab', '#ffeaa8', '#ffeda4',
			'#ffefa1', '#fff29e', '#fff49a', '#fff797', '#fffb94', '#fffe90',
			'#fcff8d', '#f8ff8a', '#f4ff86', '#f0ff83', '#ebff80', '#e7ff7c',
			'#e2ff79', '#ddff76', '#d7ff72', '#d2ff6f', '#ccff6c', '#c6ff68',
			'#bfff65', '#b9ff62', '#b2ff5e', '#abff5b', '#a4ff58', '#9dff54',
			'#95ff51', '#8dff4e', '#85ff4a', '#7dff47', '#75ff44', '#6cff40',
			'#63ff3d', '#5aff3a', '#51ff36', '#47ff33', '#3eff30', '#34ff2c',
			'#2aff29', '#26ff2c', '#22ff30', '#1fff34', '#1cff38', '#18ff3d',
			'#15ff42', '#11ff47', '#0eff4c', '#0bff51', '#07ff57', '#04ff5d',
			'#01ff63', '#00fc69', '#00f970', '#00f677', '#00f27d', '#00ef83',
			'#00ec89', '#00e88e', '#00e594', '#00e299', '#00de9e', '#00dba3',
			'#00d8a7', '#00d4ab', '#00d1af', '#00ceb3', '#00cab7', '#00c7ba',
			'#00c4be', '#00c0c0', '#00b7bd', '#00adba', '#00a4b6', '#009cb3',
			'#0093b0', '#008bac', '#0082a9', '#007ba6', '#0073a2', '#006b9f',
			'#00649c', '#005d98', '#005695', '#004f92', '#00498e', '#00438b',
			'#003d88', '#003784', '#003181', '#002c7e', '#00277a', '#002277',
			]
		self.MAX_ITERATIONS = len(self.gradients)
		self.z = 0
		self.CELL_SIZE = 20
		self.images = images
		self.len_x_axis = self.len_y_axis = 640
		self.minx = self.images[image]['centerX'] - (self.images[image]['axisLen'] / 2.0)
		self.maxx = self.images[image]['centerX'] + (self.images[image]['axisLen'] / 2.0)
		self.miny = self.images[image]['centerY'] - (self.images[image]['axisLen'] / 2.0)
		self.maxy = self.images[image]['centerY'] + (self.images[image]['axisLen'] / 2.0)
		self.pixelsize = abs(self.maxx - self.minx) / self.len_x_axis

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
				self.canvas.create_rectangle(col, self.len_x_axis-row, col+self.CELL_SIZE, self.len_y_axis-row+self.CELL_SIZE, fill=color)

	def draw(self):

		# Set up the GUI so that we can paint the fractal image on the screen
		self.window = Tk()

		self.canvas = Canvas(self.window, width=self.len_x_axis, height=self.len_y_axis, bg=self.gradients[-1])
		self.canvas.pack()

		# Paint the cell under the mouse cursor upon ordinary left click
		self.canvas.bind("<Button-1>", self.paintCell)

		# Display the entire image on the screen upon right click or spacebar
		self.canvas.bind("<Button-3>", self.paintEntireImage)
		self.window.bind("<space>", self.paintEntireImage)

		# Quit upon Esc
		self.window.bind("<Escape>", sys.exit)

		mainloop()


mandels = FractalData()
images = mandels.get_mandelbrot_dic()


def main():
	if len(sys.argv) < 2:
		print("Usage: mandelbrot.py FRACTALNAME")
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
