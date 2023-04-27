class Actor:
	def __init__(self, name):
		self.hp = 10
		self.name = name
		self.mp = 10

class Item:
	def __init__(self, name):
		self.name = name
		self.hp_effect = 0
		self.mp_effect = 0

class Party:
	def __init__(self):
		self.actors=[]
		self.inventory = []
	def addMember(self, actor):
		self.actors.append(actor)