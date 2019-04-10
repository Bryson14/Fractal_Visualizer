from julia import Julia
from mandelbrot import Mandelbrot
from Config import FractalData
import sys
from GradientFactory import GradientFactory


def main():
	fractals = FractalData()
	grads = GradientFactory()
	fracs = fractals.get_dic()
	gradients = grads.get_gradients()


	if len(sys.argv) < 2:
		print("Usage: main.py [FRACTALNAME] [GRADIENTNAME]")
		print("Where FRACTALNAME is one of:")
		for name in fracs['julia']:
			print(f"\t{name}")
		for name in fracs['mandels']:
			print(f"\t{name}")
		for name in fracs['burningshipjulia']:
			print(f"\t{name}")
		sys.exit(1)

	elif str(sys.argv[1]).lower() not in mandels and str(sys.argv[1]).lower() not in julias:
		print(f"ERROR: {sys.argv[1]} is not a valid fractal")
		print("Please choose one of the following:")
		for name in julias:
			print(f"\t{name}")
		for name in mandels:
			print(f"\t{name}")
		sys.exit(1)

	elif str(sys.argv[2]).lower() not in gradients:
		print(f"ERROR: {sys.argv[2]} is not a valid fractal")
		print("Please choose one of the following or let the program randomly choose")
		for grad in gradients:
			print(f"\t{grad}")
		sys.exit(1)

	else:
		image = str(sys.argv[1]).lower()
		grad = str(sys.argv[2]).lower()

	if image in mandels:
		Mandelbrot(mandels, image, colors).draw()
	else:
		Julia(julias, image, colors).draw()


if __name__ == '__main__':
	main()
