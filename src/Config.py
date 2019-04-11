import os
import sys


class FractalData:
	def __init__(self, data_dir='data'):
		self.data_dir = data_dir
		if 'src' in os.getcwd():
			self.data_directory = f'..\{self.data_dir}'
		else:
			self.data_directory = f'{self.data_dir}'
		self.fractals = {}
		self.os_walk()

	def os_walk(self):
		# gives os.walk the right dir based on if run from cmd line or IDE
		for root, dirs, files in os.walk(self.data_directory):
			for fil in files:
				fil = os.path.join(root, fil)
				self.index_data(fil)

	def index_data(self, fil):
		name = fil.split('\\')[-1][:-5]  # strips just name from full file name
		creal = cimag = pixels = centerx = centery = axislength = iterations = frac_type = None
		try:
			for line in open(fil):
				if line.startswith('creal'):
					creal = float(line.split(" ")[-1].strip())
				elif line.startswith('type'):
					frac_type = str(line.split(" ")[-1].strip())
				elif line.startswith('cimag'):
					cimag = float(line.split(" ")[-1].strip())
				elif line.startswith('pixel'):
					pixels = int(line.split(" ")[-1].strip())
				elif line.startswith('centerx'):
					centerx = float(line.split(" ")[-1].strip())
				elif line.startswith('centery'):
					centery = float(line.split(" ")[-1].strip())
				elif line.startswith('axislength'):
					axislength = float(line.split(" ")[-1].strip())
				elif line.startswith('iterations'):
					iterations = int(line.split(" ")[-1].strip())
		except TypeError:
			print(f"Incorrect data type in file {fil}. Check the file.")
			sys.exit(1)
		except FileNotFoundError:
			print(f"File {fil} not found. Check file and directory location.")
			sys.exit(1)

		data = Data(name, frac_type, pixels, centerx, centery, axislength, iterations, creal, cimag)
		self.fractals[name] = data.__dict__()

	def get_dic(self):
		return self.fractals

	def get_one_frac(self, name):
		name = (str(name).split("."))[0]  # in case the user asks for a file name and not just the name
		if name.lower() in self.fractals:
			return self.fractals[name.lower()]
		else:
			print("Incorrect fractal name given.")


class Data:
	def __init__(self, name, frac_type, pixels, centerx, centery, axislength, iterations, creal=None, cimag=None):
		self.dic = {
			'name':name,
			'type':frac_type,
			'centerx': centerx,
			'centery': centery,
			'axisLength': axislength,
			'iterations': iterations,
			'pixels': pixels,
			'creal': creal,
			'cimag': cimag
		}

	def __dict__(self):
		return self.dic

print(os.getcwd())