class complex:

	
	def __init__(self, real, img):
		self.real = real
		self.img = img

	def add(self, b):
		res = complex(0,0)
		res.real = self.real + b.real
		res.img = self.img + b.img
		return res

	def display(self):
		if self.img>=0:
			print("{} + i{}".format(self.real, self.img))
		if self.img<0:
			print("{} - i{}".format(self.real, -self.img))

	def conjugate(self):
		res = complex(0,0)
		res.img = -self.img
		res.real = self.real
		return res

a = complex(1,2)
b = complex(-3,-4)

