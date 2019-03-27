from julia import Julia
from mandelbrot import Mandelbrot
from fractal_data import FractalData
import sys


def main():
	fractals = FractalData()
	mandels = fractals.get_mandelbrot_dic()
	julias = fractals.get_julia_dic()

	if len(sys.argv) < 2:
		print("Usage: mandelbrot.py FRACTALNAME")
		print("Where FRACTALNAME is one of:")
		for name in mandels:
			print(f"\t{name}")
		print("Usage: julia.py FRACTALNAME")
		print("Where FRACTALNAME is one of:")
		for name in julias:
			print(f"\t{name}")
		sys.exit(1)

	elif str(sys.argv[1]).lower() not in mandels or julias:
		print(f"ERROR: {sys.argv[1]} is not a valid fractal")
		print("Please choose one of the following:")
		for name in julias:
			print(f"\t{name}")
		for name in mandels:
			print(f"\t{name}")
		sys.exit(1)

	else:
		image = str(sys.argv[1]).lower()

	if image in mandels:
		Mandelbrot(mandels, image).draw_mandelbrot()
	else:
		Julia(julias, image).draw_julia()


if __name__ == '__main__':
	main()
