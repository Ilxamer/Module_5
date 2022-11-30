#Task_3.1

from random import randint

class Warrior:
	def __init__(self,health,endurance,armor):
		self.health = health
		self.endurance = endurance
		self.armor = armor
		
	#Атака
	def attack(self,other,randomNum):
		if randomNum == 0:
			self.endurance -= 10
		elif randomNum == 1:
			other.endurance -= 10
		elif randomNum == 2:
			self.health -= randint(10,30)
			self.endurance -= 10
			other.health -= randint(10,30)
			other.endurance -= 10
		else:
			pass


		return {'Warrior1': {'Health':self.health,'Endurance':self.endurance},
		'Warrior2':{'Health':other.health,'Endurance':other.endurance}}

	#Защита
	def defend(self,other,randomNum):
		if randomNum == 0:
			other.health -= randint(0,20)
			other.armor -= randint(0,10)
			if other.armor <= 0:			 ##Случай, когда кончаются очки брони или выносливости
				other.health -=randint(10,30)
			elif self.endurance	<= 0:
				other.health -= randint(0,10)
		elif randomNum == 1:
			self.health -= randint(0,20)
			self.armor -= randint(0,10)
			if self.armor <= 0:
				self.health -=randint(10,30)
			elif other.endurance <= 0:
				self.health -= randint(0,10)
		else:
			pass

		return{'Health_1': self.health, 'Armor_1':self.armor,
		'Health_2':other.health,'Armor_2':self.armor}

	def forgive(self):
		kill = input('Убить соперника?: ')
		if kill == 'yes':
			print('Соперник убит!')
		else:
			print('Вы благородный воин!')





		
warrior1 = Warrior(100,100,100)
warrior2 = Warrior(100,100,100)


round_number = 1

while 1:
	print(f'Раунд: {round_number}')
	randomNum = randint(0,3)
	damage = warrior1.attack(warrior2,randomNum)
	defence = warrior1.defend(warrior2,randomNum)
	print(damage)
	print(defence)
	if damage['Warrior1']['Health'] <= 10:
		print('Warrior2 одержал победу!')
		warrior1.forgive()
		break
	elif damage['Warrior2']['Health'] <= 10:
		print('Warrior1 одержал победу!')
		warrior2.forgive()

		break
	round_number += 1

