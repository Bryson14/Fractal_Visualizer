class Gradients(object):
	def __new__(cls, *args, **kwargs):
		if cls is Gradients:
			raise TypeError("\nBase class of Gradients cannot be instantiated!")
		return object.__new__(cls)

	def get_gradients(self):
		pass

	def get_color(self, n):
		pass
