from tkinter import Tk, Canvas, PhotoImage
import sys


class ImagePainter:
	def __init__(self, window_width, window_height, background_color):
		self.window = Tk()
		self.img = PhotoImage(width=window_width, height=window_height)
		self.canvas = Canvas(self.window, width=window_width, height=window_height, bg=background_color)
		self.canvas.create_image((window_width // 2, window_height // 2), image=self.img, state="normal")
		self.canvas.pack()
		self.window.bind("<Escape>", sys.exit)
