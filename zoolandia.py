class Animal(object):
	'''sets up the initial object creation
	'''

	def __init__(self, name, height, weight,species):
		self.name = name
		self.height = height
		self.weight = weight
		self.species = species

	def get_name(self):
		return self.name

	def get_height(self):
		return self.height



class ElaphodusCephalophus(Animal):
	
	'''creates a new subclass of animal
	defines unique species attributes
	'''

 	def __init__(self, name, legs, tufts):
 		self.legs = legs
 		self.tufts = tufts
 	    	Animal.__init__(self, name, '30in', '30lbs', 'Elaphodus Cephalophus')



evil_bambi = ElaphodusCephalophus("evil_bambi", 4, True)

print(vars(evil_bambi))
print(evil_bambi.__dict__.values())
print(isinstance(evil_bambi,Animal))



class  PanTroglodytes(Animal):

	'''creates a new subclass of animal
	defines unique species attributes
	'''

	def __init__(self, name, legs, arms):
		self.legs = legs
		self.arms = arms
		Animal.__init__(self, name, '40 in', '60lbs', 'Pan Troglodytes')

roger = PanTroglodytes("roger", 2, 2)

print(vars(roger))
print(roger.__dict__.values())
print(isinstance(roger,Animal))

class BuboVirginianus(Animal):

	'''creates a new subclass of animal
	defines unique species attributes
	'''

	def __init__(self,name,flies,isAwesome):
		self.flies = flies
		self.isAwesome = isAwesome
		Animal.__init__(self, name, '16in', '8lbs', 'Bubo Virginianus')

watson = BuboVirginianus("watson", True, True)

print(vars(watson))
print(watson.__dict__.values())
print(isinstance(watson,Animal))
















