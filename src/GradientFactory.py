from mountains import Mountains
from funkyfresh import Funkyfresh


class GradientFactory:
	def __init__(self, args='default', iterations=96):
		if isinstance(args, list):
			self.args = args
		if isinstance(args, str):
			self.args = args.lower()
		self.iterations = iterations

	def makeGradient(self):
		if self.args == 'default':
			return Funkyfresh(self.iterations)
		if self.args == 'mountains':
			return Mountains(self.iterations)
