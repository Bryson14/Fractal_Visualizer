from ImagePainter import ImagePainter


class Fractal(object):
	def __init__(self, image, colors):
		self.gradients = colors
		self.image = image
		self.len_x_axis = self.len_y_axis = 640
		self.minx = image['centerx'] - (image['axisLength'] / 2.0)
		self.maxx = image['centerx'] + (image['axisLength'] / 2.0)
		self.miny = image['centery'] - (image['axisLength'] / 2.0)
		self.maxy = image['centery'] + (image['axisLength'] / 2.0)
		self.pixel_size = abs(self.maxx - self.minx) / self.len_x_axis
		self.image_painter = ImagePainter(self.len_x_axis, self.len_y_axis, self.gradients[-1])

	def __new__(cls, *args, **kwargs):
		if cls is Fractal:
			raise TypeError("\nBase class of Fractal cannot be instantiated!")
		return object.__new__(cls)

	def count(self, z: complex) ->int:
		pass

	def paint(self):
		pass

	def draw(self):
		pass
