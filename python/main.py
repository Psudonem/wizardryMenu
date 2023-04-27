class Npc:
	def __init__(self, name, talk):
		self.name=name
		self.talk=talk

class Weapon:
	def __init__(self, name):
		self.name = name

class Actor:
	def __init__(self, name):
		self.hp = 10
		self.name = name
		self.mp = 10
		self.weapon= None
	def equipWeapon(self,weapon):
		self.weapon = weapon

class Item:
	def __init__(self, name):
		self.name = name
		self.hp_effect = 0
		self.mp_effect = 0

class Party:
	def __init__(self):
		self.actors=[]
		self.inventory = []
		self.money = 1000
	def addMember(self, actor):
		self.actors.append(actor)

def main():
	print("Welcome to the Town")
	print("1) Bar") # get/fire party members
	print("2) Armory") # buy weapons 
	print("3) Items") # buy items
	print("4) Talk") #talk to npcs

main()