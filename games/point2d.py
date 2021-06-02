import math
''' Drawings a dot in 2-ds '''
class point:
	def __init__(self, x=0, y=0):
		self.move(x, y)
	
	def move(self, x, y):
		self.x = x
		self.y = y
	
	def reset(self):
		self.move(0, 0)
	
	def calculate_distance(self, other_point):
		return math.sqrt((self.x - other_point.x)**2 + 
		                  (self.y - other_point.y)**2)
