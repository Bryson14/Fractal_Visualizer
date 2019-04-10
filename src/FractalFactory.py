from Config import FractalData


class FractalFactory:
	def __new__(cls, *args, **kwargs):
		if cls is FractalFactory:
			raise TypeError("\nBase class of FractalFactory cannot be instantiated!")
		return object.__new__(cls)

	def __init__(self):
		self.necessary_mandelbrot_data = {'pixels', 'iterations', 'centerx', 'centery', 'axislength'}
		self.necessary_julia_data = {'pixels', 'iterations', 'centerx', 'centery', 'axislength', 'creal', 'cimag'}
		self.necessary_burningship_data = set([])
		self.necessary_phoenix_data = set([])

	def makeFractal(self, file):
		frac_data = FractalData().index_data(file)
		self.verify_data(frac_data)
		return frac_data

	def verify_data(self, indexed_data):
		if indexed_data['type'] == 'mandelbrot':
			for piece_o_data in self.necessary_mandelbrot_data:
				if piece_o_data not in indexed_data:
					raise NotImplemented(
						f"{piece_o_data} data field not correctly filled for this {indexed_data['type']} fractal")
		elif indexed_data['type'] == 'julia':
			for piece_o_data in self.necessary_julia_data:
				if piece_o_data not in indexed_data:
					raise NotImplemented(
						f"{piece_o_data} data field not correctly filled for this {indexed_data['type']} fractal")
		elif indexed_data['type'] == 'burningship':
			for piece_o_data in self.necessary_burningship_data:
				if piece_o_data not in indexed_data:
					raise NotImplemented(
						f"{piece_o_data} data field not correctly filled for this {indexed_data['type']} fractal")
		elif indexed_data['type'] == 'phoenix':
			for piece_o_data in self.necessary_phoenix_data:
				if piece_o_data not in indexed_data:
					raise NotImplemented(
						f"{piece_o_data} data field not correctly filled for this {indexed_data['type']} fractal")
		else:
			raise NotImplemented(
				f"data file not found in data directory")
