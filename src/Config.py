import os


class FractalData:
	def __init__(self, data_dir='data'):
		self.data_dir = data_dir
		self.mandelbrot_types = {}
		self.julia_types = {}
		self.burningship_types = {}
		self.index_data()

	def index_data(self):
		# gives os.walk the right dir based on if run from cmd line or IDE
		print(os.getcwd())
		if 'src' in os.getcwd():
			data_directory = f'..\{self.data_dir}'
		else:
			data_directory = f'{self.data_dir}'

		for root, dirs, files in os.walk(data_directory):
			for fil in files:
				fil = os.path.join(root, fil)
				for line in open(fil):
					if line.startswith('#'):
						pass
					elif line.startswith('type') and 'burning' in line:
						self.index_julia(fil, True)
					elif line.startswith('type') and 'julia' in line:
						self.index_julia(fil)
					elif line.startswith('type') and 'mandelbrot' in line:
						self.index_mandelbrot(fil)

	def index_mandelbrot(self, fil):
		name = fil.split('\\')[-1][:-5]  # strips just name from full file name
		pixels = centerX = centerY = axislength = iterations = 0
		for line in open(fil):
			if line.startswith('pixel'):
				pixels = int(line.split(" ")[-1].strip())
			elif line.startswith('centerx'):
				centerX = float(line.split(" ")[-1].strip())
			elif line.startswith('centery'):
				centerY = float(line.split(" ")[-1].strip())
			elif line.startswith('axislength'):
				axislength = float(line.split(" ")[-1].strip())
			elif line.startswith('iterations'):
				iterations = int(line.split(" ")[-1].strip())

		mandel = Mandelbrot(pixels, centerX, centerY, axislength, iterations)
		self.mandelbrot_types[name] = mandel.__dict__()


	def index_julia(self, fil, burningship = False):
		name = fil.split('\\')[-1][:-5]  # strips just name from full file name
		creal = cimag = pixels = centerX = centerY = axislength = iterations = 0
		for line in open(fil):
			if line.startswith('creal'):
				creal = float(line.split(" ")[-1].strip())
			elif line.startswith('cimag'):
				cimag = float(line.split(" ")[-1].strip())
			elif line.startswith('pixel'):
				pixels = int(line.split(" ")[-1].strip())
			elif line.startswith('centerx'):
				centerX = float(line.split(" ")[-1].strip())
			elif line.startswith('centery'):
				centerY = float(line.split(" ")[-1].strip())
			elif line.startswith('axislength'):
				axislength = float(line.split(" ")[-1].strip())
			elif line.startswith('iterations'):
				iterations = int(line.split(" ")[-1].strip())

		if not burningship:
			julia = Julia(creal, cimag, pixels, centerX, centerY, axislength, iterations)
			self.julia_types[name] = julia.__dict__()
		else:
			burning = BurningShip(creal, cimag, pixels, centerX, centerY, axislength, iterations)
			self.burningship_types[name] = burning.__dict__()

	def get_mandelbrot_dic(self):
		return self.mandelbrot_types

	def get_julia_dic(self):
		return self.julia_types

	def get_Burningship_dic(self):
		return self.burningship_types


class Mandelbrot:
	def __init__(self, pixels, centerX, centerY, axislength, iterations):
		self.pixels = pixels
		self.centerX = centerX
		self.centerY = centerY
		self.axislength = axislength
		self.iterations = iterations

	def __dict__(self):
		dic = {
			'pixels': self.pixels,
			'centerX': self.centerX,
			'centerY': self.centerY,
			'axisLen': self.axislength,
			'iterations': self.iterations
		}
		return dic


class Julia:
	def __init__(self, creal, cimag, pixels, centerX, centerY, axislength, iterations):
		self.creal = creal
		self.cimag = cimag
		self.pixels = pixels
		self.centerX = centerX
		self.centerY = centerY
		self.axislength = axislength
		self.iterations = iterations

	def __dict__(self):
		dic = {
			'creal': self.creal,
			'cimag': self.cimag,
			'centerX': self.centerX,
			'centerY': self.centerY,
			'axisLength': self.axislength,
			'iterations': self.iterations
		}
		return dic


class BurningShip:
	def __init__(self, creal, cimag, pixels, centerX, centerY, axislength, iterations):
		self.creal = creal
		self.cimag = cimag
		self.pixels = pixels
		self.centerX = centerX
		self.centerY = centerY
		self.axislength = axislength
		self.iterations = iterations

	def __dict__(self):
		dic = {
			'creal': self.creal,
			'cimag': self.cimag,
			'centerX': self.centerX,
			'centerY': self.centerY,
			'axisLength': self.axislength,
			'iterations': self.iterations
		}
		return dic
