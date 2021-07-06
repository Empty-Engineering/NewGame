#Initiate the possible characteristics for the character
class Character:
	def __init__(self, name, health, points, characterType)->None:
		self.characterType = characterType
		self.name = name
		self.health = health
		self.points = points
	def get_characterType(self)->object:
		return self.characterType
	def get_health(self)->object:
		return self.damage
	def get_points(self)->object:
		return self.points
class Villain(Character):
	def set_characterType():
		characterType = 'villain'
	def get_characterType(self)->object:
		return self.characterType
	def get_damage(self)->object:
		return self.damage
	def get_health(self)->object:
		return self.health
	def get_points(self)->object:
		return self.points
class Hero(Character):
	def set_characterType(self)->None:
		self.characterType = 'hero'
	def get_characterType(self)->object:
		return self.characterType
	def get_health(self)->object:
		return self.health
	def get_points(self)->object:
		return self.points
#Function Comparing the greater of points
def greater_points()->object:
	if characterHero.get_points()>characterVillain.get_points():
		return characterHero
	elif characterVillain.get_points()>characterHero.get_points():
		return characterVillain
#Main Game body
def gameBody()->None:
	rounds = 0
	print("Welcome to the game! ")
	print("-----------------------------------")
	global characterHero
	characterHero = Hero("", 0, 0, 'hero')
	characterHero.health = 100
	nameHero = input(f"Enter your {characterHero.characterType}'s name: ")
	characterHero.name = nameHero
	global characterVillain
	characterVillain = Villain("", 0, 0, 'villain')
	characterVillain.health = 100
	nameVillain = input(f"Enter your {characterVillain.characterType}'s name: ")
	characterVillain.name = nameVillain
	moveEffectNum = {"punch": 10, "cast spell": 2, "siege": 1}
#Game loop for 20 rounds
	while (rounds<20):
		rounds += 1
		while rounds>0:
			return
		heroMove = input(f"What is {characterHero.name}'s move? (Punch, Cast spell, or Siege?) ")
		if heroMove.lower() == "punch":
			characterVillain.health -= moveEffectNum[heroMove.lower()]
			characterHero.points += 5
			print(f"The character stats changed are:\n {characterHero.name}'s points: {characterHero.points}\n {characterVillain.name}'s health: {characterVillain.health}")
			
		elif heroMove.lower() == "cast spell" or heroMove.lower() == "spell":
			characterVillain.health -= moveEffectNum[heroMove.lower()]
			characterHero.health += 2
			print(f"The character stats changed are:\n {characterHero.name}'s points: {characterHero.points}\n {characterVillain.name}'s health: {characterVillain.health}")
			
		elif heroMove.lower() == "siege":
			if characterVillain.get_points()>=1:
				characterVillain.points -= moveEffectNum[heroMove.lower()]
			characterHero.points += 1
			print(f"The character stats changed are:\n {characterHero.name}'s points: {characterHero.points}\n {characterVillain.name}'s points: {characterVillain.points}")
		if characterVillain.get_health() <= 0:
			print(f"Hero wins because {characterVillain.name}'s health fell below 0")
			break
			
		villainMove = input(f"What is {characterHero.name}'s move? (Punch, Cast spell, or Siege?) ")
		if villainMove.lower() == "punch":
			characterHero.health -= moveEffectNum[villainMove.lower()]
			characterVillain.points += 5
			print(f"The character stats changed are:\n {characterHero.name}'s points: {characterVillain.points}\n {characterHero.name}'s health: {characterHero.health}")
			
		elif villainMove.lower() == "cast spell" or villainMove.lower() == "spell":
			characterHero.health -= moveEffectNum[villainMove.lower()]
			characterVillain.health += 2
			print(f"The character stats changed are:\n {characterHero.name}'s points: {characterHero.points}\n {characterVillain.name}'s health: {characterVillain.health}")
			
		elif villainMove.lower() == "siege":
			if characterHero.get_points()>=1:
				characterHero.points -= moveEffectNum[villainMove.lower()]
			characterVillain.points += 1
			print(f"The character stats changed are:\n {characterHero.name}'s points: {characterHero.points}\n {characterVillain.name}'s points: {characterVillain.points}")
		if characterHero.get_health() <= 0:
			print(f"Villain wins because {characterHero.name}'s health fell below 0")
			break
#What to do if 20 rounds pass and both character's healths are above 0
	greaterPoints = greater_points()
	if rounds >= 20:
		print(f"{greaterPoints.name} wins the game with {greaterPoints.points}")
			
gameBody()
