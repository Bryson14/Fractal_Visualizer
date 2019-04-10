import os


class FractalData:
	def __init__(self, data_dir='data'):
		self.data_dir = data_dir
		self.fractals = {}
		self.os_walk()

	def os_walk(self):
		# gives os.walk the right dir based on if run from cmd line or IDE
		print(os.getcwd())
		if 'src' in os.getcwd():
			data_directory = f'..\{self.data_dir}'
		else:
			data_directory = f'{self.data_dir}'

		for root, dirs, files in os.walk(data_directory):
			for fil in files:
				fil = os.path.join(root, fil)
				self.index_data(fil)

	def index_data(self, fil):
		name = fil.split('\\')[-1][:-5]  # strips just name from full file name
		creal = cimag = pixels = centerX = centerY = axislength = iterations = frac_type = None
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
				centerX = float(line.split(" ")[-1].strip())
			elif line.startswith('centery'):
				centerY = float(line.split(" ")[-1].strip())
			elif line.startswith('axislength'):
				axislength = float(line.split(" ")[-1].strip())
			elif line.startswith('iterations'):
				iterations = int(line.split(" ")[-1].strip())

		data = Data(frac_type, pixels, centerX, centerY, axislength, iterations, creal, cimag)
		self.fractals[name] = data.__dict__()

	def get_dic(self):
		return self.fractals


class Data:
	def __init__(self, frac_type, pixels, centerx, centery, axislength, iterations, creal=None, cimag=None):
		self.dic = {
			'type':frac_type,
			'centerX': centerx,
			'centerY': centery,
			'axisLength': axislength,
			'iterations': iterations,
			'pixels': pixels,
			'creal': creal,
			'cimag': cimag
		}

	def __dict__(self):
		for key in self.dic:
			if not self.dic[key]:
				self.dic.pop(key)
		return self.dic
