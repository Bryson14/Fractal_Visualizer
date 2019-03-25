import os

class FractalData:
	def __init__(self):
		self.mandelbrot_types = {}
		self.julia_types = {}

	def index_data(self):
		for fil in os.walk(r'..\data'):
			for line in open(fil):
				if line.startswith('#'):
					pass
				elif line.startswith('type') and 'julia' in line:
					self.index_julia(fil)
				elif line.startswith('type') and 'mandelbrot' in line:
					self.index_mandelbrot(fil)

	def index_mandelbrot(self, fil):
		pass

	def index_julia(self, fil):
		pass

class Mandelbrot:
	def __init__(self, name, pixels, centerX, centerY, axislength, interations):
		self.name = name
		self.pixels = pixels
		self.centerX = centerX
		self.centerY = centerY
		self.axislength = axislength
		self.interations = interations

	def __dict__(self):
		print("runnning")
		dic = {
			'centerX': self.centerX,
			'centerY': self.centerY,
			'axisLen': self.axislength,
			'iterations': self.interations
		}
		return {self.name: dic}


class Julia:
	def __init__(self, name, creal, cimag, pixels, centerX, centerY, axislength, interations):
		self.name = name
		self.creal = creal
		self.cimag = cimag
		self.pixels = pixels
		self.centerX = centerX
		self.centerY = centerY
		self.axislength = axislength
		self.interations = interations

	def __dict__(self):
		dic = {
			'creal': self.creal,
			'cimag': self.cimag,
			'centerX': self.centerX,
			'centerY': self.centerY,
			'axisLen': self.axislength,
			'iterations': self.interations
		}
		return {self.name: dic}





