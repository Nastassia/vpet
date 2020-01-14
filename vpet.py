from foods import * 
from random import randrange

class Monster:
	
	def __init__(self,name,species):
		self.name = name
		self.species = species
		self.happiness = 50
		self.hunger = 50
		self.fav_food = []
		self.hated_food = []
		self.status = {}

		def fav_foods(self,foodsdb):
			for i in foodsdb.keys():
				num_items = len(foodsdb[i]) - 1
				self.fav_food.append(foodsdb[i][randrange(num_items)])
		
		def hated_foods(self,foodsdb):
			for i in foodsdb.keys():
				num_items = len(foodsdb[i]) - 1
				food = foodsdb[i][randrange(num_items)]
				if food in self.fav_food:
					food = foodsdb[i][randrange(num_items)]
				
				self.hated_food.append(food)


		fav_foods(self,foodsdb)
		hated_foods(self,foodsdb)	

	def info(self):
		m_info = {"Name": self.name, "Species": self.species, "Hunger": self.hunger, "Happiness": self.happiness, "Favorite Foods": self.fav_food, "Hated Foods": self.hated_food}
		return m_info

	
blop = Monster("Blop","Bear")
abraxas = Monster("Abraxas","Dragon")

print(blop.info())
print(abraxas.info())	
print()



#print("random key code now")
#print(random.choice(list(foodsdb.keys())))
