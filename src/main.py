#!/bin/env python3

import sys
from GradientFactory import GradientFactory
from FractalFactory import FractalFactory


def main():
	usage = "python src/main.py [FRACTAL_FILE [GRADIENT_NAME]]\n python src\main.py help [fractals][gradients]"
	if len(sys.argv) < 2:
		print("\tFractalFactory: Creating default fractal\n\tGradientFactory: Creating default color gradient")
		gradients = GradientFactory().makeGradient().get_gradients()
		fractal = FractalFactory().makeFractal(gradients)
		fractal.draw()

	elif len(sys.argv) == 2:
		if sys.argv[1] == 'help':
			print(usage)
		else:
			print("\tGradientFactory: Creating default color gradient")
			gradients = GradientFactory().makeGradient().get_gradients()
			fractal = FractalFactory().makeFractal(gradients, sys.argv[1])
			fractal.draw()

	elif len(sys.argv) == 3:
		if sys.argv[1] == 'help':
			print(usage)
		else:
			gradients = GradientFactory(sys.argv[2]).makeGradient().get_gradients()
			fractal = FractalFactory().makeFractal(gradients, sys.argv[1])
			fractal.draw()
	else:
		print(usage)


if __name__ == '__main__':
	main()
