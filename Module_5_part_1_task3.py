#Task_3.1

# import random 

# class Warrior():
# 	def __init__(self,name):
# 		self.name = name
# 		self.health = 100
# 	def attack(self,other):
# 		while self.health != 0 or other.health != 0:
# 			i = 1
# 			print(f'Раунд {i} начался: ')
# 			for i in random.choice((self.name,other.name)):
# 				if random.choice == self.name:
# 					self.health -= 20
# 					print('Здоровья у воина ' + self.name + ' стало меньше на 20 единиц.' )
# 				else:
# 					other.health -= 20
# 					print('Здоровья у воина ' + other.name + ' стало меньше на 20 единиц.')

# 			print(f'Раунд {i} завершился!')
# 			i += 1 



# warrior1 = Warrior('Drakula')
# warrior2 = Warrior('Master')

# warrior1.attack(warrior2)


#Task_3.1

from random import randint

class Warrior():
	def __init__(self,health):
		self.health = health
		
	def attack(self,other,randomNum):
		if randomNum == 0:
			self.health -= 20
		else:
			other.health -= 20
		return [self.health,other.health]

		
warrior1 = Warrior(100)
warrior2 = Warrior(100)

while 1:
	round_number = 1
	print(f'Раунд: {round_number}')
	randomNum = randint(0,1)
	damage = warrior1.attack(warrior2,randomNum)
	print(damage)
	if damage[0] <= 0:
		print('Warrior2 одержал победу!')
		break
	elif damage[1] <= 0:
		print('Warrior1 одержал победу!')
		break
	round_number += 1




















