from Gradient import Gradients
from colour import Color


class Mountains(Gradients):
	def __init__(self, iterations):
		start = Color('#014421')  # forest green
		start2 = Color('#87ceeb')  # sky blue
		start3 = Color('#7d3f33')  # red rock red
		chunk = iterations // 3
		self.grads = list(start.range_to(start2, chunk)) + list(start2.range_to(start3, chunk)) + \
			list(start3.range_to(start, chunk))

	def get_gradients(self):
		return self.grads

	def get_color(self, n):
		return self.grads[n]
