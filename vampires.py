class Vampire:
	""" A class that defines the aspects of a Vampire object """

	coven = []
	# in_coffin = True
	# drank_blood_today = False
	
	def __init__(self, name, age):
		self.name = name
		self.age = age
		self.in_coffin = True
		self.drank_blood_today = False

	def __str__(self):
		return f"{self.name}, {self.age}, {self.in_coffin}, {self.drank_blood_today}"

	def __repr__(self):
		return f"{self.name}, {self.age}, {self.in_coffin}, {self.drank_blood_today}"

	@classmethod
	def create(cls, name, age):
		vampire = Vampire(name, age)
		cls.coven.append(vampire)
		return vampire

	def drink_blood(self):
		self.drank_blood_today = True

	@classmethod
	def sunrise(cls):
		culllist = []
		for vampire in Vampire.coven:
			if vampire.in_coffin is False or vampire.drank_blood_today is False:
				culllist.append(vampire)

		for vampire in culllist:
			Vampire.coven.remove(vampire)

	@classmethod
	def sunset(cls):
		print("\nIt's a terrible night for a curse.\n")
		for vampire in Vampire.coven:
			vampire.drank_blood_today = False
			vampire.in_coffin = False

	def go_home(self):
		self.in_coffin = True


nosferatu = Vampire.create('Nosferatu', 3000)
dracula = Vampire.create('Dracula', 1500)
molloy = Vampire.create('Daniel Molloy', 430)

print(Vampire.coven)

Vampire.sunset()

print(Vampire.coven)

nosferatu.drink_blood()
dracula.drink_blood()
molloy.drink_blood()

print(Vampire.coven)

nosferatu.go_home()

print(Vampire.coven)

Vampire.sunrise()

print(Vampire.coven)





# if vampire.in_coffin is False or vampire.drank_blood_today is False:
			# 	Vampire.coven.remove(vampire)