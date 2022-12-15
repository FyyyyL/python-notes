

class PAINTER:

	def __init__(self):
		self.pixs = []
		self.x_size = 50
		self.y_size = 30
		# pixs = [[x,y],[x,y]]

	def draw(self):
		sign_for_new_line = True

		for x in range(self.x_size):
			print("-",end="")

		for x in range(self.x_size):
			sign_for_new_line = True
			for y in range(self.y_size):
				if sign_for_new_line:
					sign_for_new_line=False
					# the x and y not correct!!!
					# be care !!!!!!!!!!!!!!!!!!!!
					if [y,x] in self.pixs:
						print("\n*",end="")
					else:
						print("\n ",end="")
				else:
					if [y,x] in self.pixs:
						print("*",end="")
					else:
						print(" ",end="")
		print("\n-",end="")		
		for x in range(self.x_size-1):
			print("-",end="")


	def insert(self,x,y):
		self.pixs.append([x,y])

	def clean(self):
		self.pixs = []


import math

painter = PAINTER()

for y in range(10):
	painter.insert(6,y)
	painter.insert(20,y)


for x in range(6,13):
	painter.insert(x,0)
	painter.insert(x,3)

for y in range(4):
	painter.insert(13,y)

for x in range(20,27):
	painter.insert(x,5)
	painter.insert(x,9)

for y in range(5,10):
	painter.insert(27,y)

painter.draw()

# (0,0) (1,0) (2,0)
# (0,1) (1,1) (2,1)
# (0,2) (1,2) (2,2)