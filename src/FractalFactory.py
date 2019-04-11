from Config import FractalData
from mandelbrot import Mandelbrot
from julia import Julia
from phoenix import Phoenix
from burningship import Burningship


class FractalFactory:
	def __init__(self):
		self.necessary_mandelbrot_data = {'pixels', 'iterations', 'centerx', 'centery', 'axislength'}
		self.necessary_julia_data = {'pixels', 'iterations', 'centerx', 'centery', 'axislength', 'creal', 'cimag'}
		self.necessary_burningship_data = set([])
		self.necessary_phoenix_data = set([])

	def makeFractal(self, gradients, file='spiral0.frac'):
		frac_data = FractalData().get_one_frac(file)
		# self.verify_data(frac_data)
		if frac_data['type'] == 'mandelbrot':
			return Mandelbrot(frac_data, gradients)
		elif frac_data['type'] == 'julia':
			return Julia(frac_data, gradients)
		elif frac_data['type'] == 'burningship':
			return Burningship(frac_data, gradients)
		elif frac_data['type'] == 'phoenix':
			return Phoenix(frac_data, gradients)

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
				f"name of fractal not found in data directory")
