#Task_3.1

import random 

class Warrior():
	def __init__(self,name):
		self.name = name
		self.health = 100
	def attack(self,other):
		while self.health != 0 or other.health != 0:
			i = 1
			print(f'Раунд {i} начался: ')
			for i in random.choice((self.name,other.name)):
				if random.choice == self.name:
					self.health -= 20
					print('Здоровья у воина ' + self.name + ' стало меньше на 20 единиц.' )
				else:
					other.health -= 20
					print('Здоровья у воина ' + other.name + ' стало меньше на 20 единиц.')

			print(f'Раунд {i} завершился!')
			i += 1 



warrior1 = Warrior('Drakula')
warrior2 = Warrior('Master')

warrior1.attack(warrior2)








