#!/bin/env python3

# Julia Set Visualizer

import sys
from tkinter import mainloop
from Config import FractalData
from ImagePainter import ImagePainter


class Julia:
	def __init__(self, images, image):
		self.image = image
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

