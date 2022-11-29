#Task_1

class StringVar:

	def __init__(self,txt):
		self.txt = txt  

	def set_txt(self, new_txt):
		self.new_txt = self.txt.replace(self.txt,new_txt)
		print(self.new_txt)


	def get_txt(self):
		print(self.txt)


txt1 = StringVar('Some text')
txt1.set_txt('Another text')
txt1.get_txt()

#Task_2

class Point():
	
	def __init__(self, x, y):
		self.x = x 
		self.y = y 

	def distance(self,other):
		return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** (1/2)

	def __add__(self, other):
		return Point (self.x + other.x, self.y + other.y)

p1_x = int(input('Enter p1_x : '))
p1_y = int(input('Enter p1_y : '))
p2_x = int(input('Enter p2_x : '))
p2_y = int(input('Enter p2_y : '))

p1 = Point(p1_x,p1_y)
p2 = Point(p2_x,p2_y)
p3 = p1 + p2

print(p3)

print(p1.distance(p2))





