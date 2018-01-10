class Myclass:
	
	def insert(self,name):
		self.name=name
	def show(self):
		print(self.name)

object=Myclass()
object.insert('shahid')
object.show()

import math
print(math.sqrt(81))
#print(dir(math))
#print(help(math))

print(dir(__package__))

