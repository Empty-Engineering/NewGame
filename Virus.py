import random
#Create class for superhero
class Characters:
#	Assign Attributes
	def __init__(self, name, points, damage, health, state):
		self.name = name
		self.points = points
		self.damage = damage
		self.health = health
		self.state = state
	def get_name(self)->object:
		return self.name
	def get_points(self)->object:
		return self.points
	def dealt_damage(self)->object:
		return self.damage
	def get_health(self):
		return self.health
	def get_state(self):
		return self.state
class Hero(Characters):
	def modOfSuperClass(self)->None:
		return
class Villain(Characters):
	def modOfSuperClass(self)->None:
		return
		
def initiateCharacters()->None:
	heroName = input("What is your hero's name? ")
	villainName = input("What is your villain's name? ")
	characterHero = Hero(heroName, 0, 10, 100, 1)
	characterVillain = Villain(villainName, 0, 10, 100, 1)
	stateKey = {0: "Dead", 1: "Alive"}
	rounds = 0
	while True:
		if characterVillain.get_points() == 100:
			print(characterVillain.get_name()+" wins the game with 100 points.\n"+
				characterVillain.get_name()+
				" had a final damage/move ratio of: "+
				str(characterVillain.dealt_damage())
			)
			break
		if characterHero.get_points() == 100:
			print(
				characterHero.get_name()+
				" wins the game with 100 points.\n"
				+characterHero.get_name()+
				" had a final damage/move ratio of: "+ 
				str(characterHero.dealt_damage())
			)
			break
		rounds += 1
		if rounds < 20:
			firstMove = random.randint(0,1)
			missChance = random.randit(0,10)
			if characterHero.get_health()>0:
				characterHero.state = 1
			if characterVillain.get_health()>0:
				characterVillain.state = 1
			if firstMove == 0:
				villainMove = ("Would you like "+characterVillain.get_name()+" to: punch, set spell, or siege?")
				if missChance != 5:
					if villainMove.lower() == "punch":
						characterHero.health -= characterVillain.dealt_damage()
						if characterHero.get_points()>10:
							characterHero.points -= 10
						characterVillain.points += 1
					elif (villainMove.lower() == "set spell") or (villainMove.lower == "spell"):
						characterVillain.damage += 2
					elif villainMove.lower() == "siege":
						if characterHero.dealt_damage()>0:
							characterHero.damage -= 1
							characterVillain.damage += 1
						else:
							print("Move failed!")
				else:
					print("Move failed!")
			else:
				heroMove = ("Would you like "+characterHero.get_name()+" to: punch, set spell, or siege?")
				if missChance != 5:
					if heroMove.lower() == "punch":
						characterVillain.health -= characterHero.dealt_damage()
						if characterVillain.get_points()>10:
							characterVillain.points -= 10
						characterHero.points += 1
					elif (heroMove.lower() == "set spell") or (heroMove.lower == "spell"):
						characterHero.damage += 2
					elif heroMove.lower() == "siege":
						if characterVillain.dealt_damage()>0:
							characterVillain.damage -= 1
							characterHero.damage += 1
						else:
							print("Move failed!")
		elif rounds >= 20:
			if characterHero.get_points()>characterVillain.get_points():
				print(
					characterHero.get_name()+
					" wins the game with 100 points.\n"
					+characterHero.get_name()+
					" had a final damage/move ratio of: "+ 
					str(characterHero.dealt_damage())
				)
				break