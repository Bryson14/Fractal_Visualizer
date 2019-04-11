from Gradient import Gradients
from colour import Color


class Funkyfresh(Gradients):
	def __init__(self, iterations):
		start = Color('#39ff14')  # bright green
		start2 = Color('#008080')  #teal
		start3 = Color('yellow')
		start4 = Color('purple')
		chunk = iterations // 4
		self.grads = list(start.range_to(start2, chunk)) + list(start2.range_to(start3, chunk))\
			+ list(start3.range_to(start4, chunk))

	def get_gradients(self):
		return self.grads

	def get_color(self, n):
		return self.grads[n]
