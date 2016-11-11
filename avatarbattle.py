#!/usr/bin/python
#SU eo-d
import random
import sys, os
class bcolors:
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	CYAN = '\033[96m'
	WHITE = '\033[97m'
	ENDC = '\033[0m'
os.system('clear')

#<def section start --

#banner
def banner():
	print("\t-------------------------- AVATAR -----------------------------")
	print("\t----------------------------- BATTLE --------------------------\n")

def attackbanner():
	print("\t-------------------------- AVATAR -----------------------------")
	print("\t----------------------------- BATTLE --------------------------\n")
	print("Your HP: " + str(playerHealth))
	print(opponent + " HP: " + str(opponentHealth))

#def rules():
#	print("\t----------------------------- RULES -----------------------------")
#	print("")

#playerselect
def playerselect():
	os.system('clear')
	print("+-------------------------+")
	print("|   SELECT YOUR FIGHTER   |")
	print("+-------------------------+")
	print("| Name    | Element       |")
	print("+-------------------------+")
	print("| Bolin   | Earth-Bender  |")
	print("|         |               |")
	print("| Katara  | Water-Bender  |")
	print("|         |               |")
	print("| Zuko    | Fire-Bender   |")
	print("|         |               |")
	print("| Tenzin  | Air-Bender    |")
	print("+-------------------------+")

# -- def section end>
playerselect()


#Select your fighter!
fighterSelect = raw_input("Select your fighter: ")
FS01 = fighterSelect
if str.lower(FS01) == "bolin":
	player = "Bolin"
	os.system('clear')
	playerselect()
	print("You selected Bolin! Are you sure?")
	lol = raw_input("(y/n): ")
	if lol == "n":
		print("Too bad.")
elif str.lower(FS01) == "katara":
	player = "Katara"
	os.system('clear')
	playerselect()
	print("You selected Katara! Are you sure?")
	lol = raw_input("(y/n): ")
	if lol == "n":
        	print("Too bad.")
elif str.lower(FS01) == "zuko":
	player = "Zuko"
	os.system('clear')
	playerselect()
	print("You selected Zuko! Are you sure?")
	lol = raw_input("(y/n): ")
	if lol == "n":
        	print("Too bad.")
elif str.lower(FS01) == "tenzin":
	player = "Tenzin"
	os.system('clear')
	playerselect()
	print("You selected Tenzin! Are you sure?")
	lol = raw_input("(y/n): ")
	if lol == "n":
        	print("Too bad.")
elif FS01 == "creds" or FS01 == "Creds":
	print("~/ James Shay.")
	quit()
else:
	quit()
os.system('clear')

banner()

#Player Health
playerHealth = 100

#Opponent Health
opponentHealth = 100

#healthCheck While Loop
healthCheck = 1

#Selecting an opponent
opponentList = ['Bolin', 'Katara', 'Zuko', 'Tenzin']
opponent = random.choice(opponentList)
if opponent == player:
	opponentList = ['Bolin', 'Katara', 'Zuko', 'Tenzin']
	opponent = random.choice(opponentList)
if opponent == player:
        opponentList = ['Bolin', 'Katara', 'Zuko', 'Tenzin']
        opponent = random.choice(opponentList)
if opponent == player:
        opponentList = ['Bolin', 'Katara', 'Zuko', 'Tenzin']
        opponent = random.choice(opponentList)

print("Your opponent will be: " + opponent)

#Fighter Moves
#Bolin: A1 - Boulder Punch, A2 - Rock Throw, D1 - Rock Wall, D2 - Dodge
#Katara: A1 - Water Whip, A2 - Ice Attack, D1 - Ice Wall, D2 - Dodge
#Zuko: A1 - Scorch, A2 - Firestorm, D1 - Melt, D2 - Dodge
#Tenzin: A1 - Wind Slice, A2 - Gust, D1 - Breeze Block, D2 - Dodge

raw_input("(Press enter to start battle..)")

#----------------------------------------------------------------------------------------------------------------------------------------------------#

os.system('clear')
attackbanner()


#1 - Block/STD Attack
#2 - Dodge/Projectile Attack
opponentGenList = [1, 1, 2]

#-----------------------------------------------------------------------------------------------
#ATTACK CODE -----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
totalLoop = 0
while totalLoop == 0:
	os.system('clear')
	attackbanner()
	print("\n\nIt's your turn! What will you do?\n")
	if player == "Bolin":
		print("1 - Boulder Punch (20 DMG, 0 DMG if blocked)")
		print("2 - Rock Throw (30 DMG, 10 DMG if blocked) [Dodgeable]")
	elif player == "Katara":
		print("1 - Water Whip (20 DMG, 0 DMG if blocked)")
		print("2 - Ice Attack (30 DMG, 10 DMG if blocked) [Dodgeable]")
	elif player == "Zuko":
		print("1 - Scorch (20 DMG, 0 DMG if blocked)")
		print("2 - Firestorm (30 DMG, 10 DMG if blocked) [Dodgeable]")
	elif player == "Tenzin":
		print("1 - Wind Slice (20 DMG, 0 DMG if blocked)")
		print("2 - Gust (30 DMG, 10 DMG if blocked) [Dodgeable]")
	opponentGen = random.choice(opponentGenList)
	playerAttack = raw_input("\nAttack (1 or 2): ")
	if playerAttack == "1" and opponentGen == 1:
		os.system('clear')
		attackbanner()
		print("\n" + opponent + " blocked! No damage was dealt!")
	elif playerAttack == "1" and opponentGen == 2:
		opponentHealth = opponentHealth - 20
		if opponentHealth <= 0:
			os.system('clear')
			print("Congratulations! " + opponent + " has been defeated! You won!")
			quit()
		elif playerHealth <= 0:
			os.system('clear')
			print("You have been defeated!")
			quit()
		os.system('clear')
		attackbanner()
		print("\n" + opponent + " failed to block attack. 20 DMG was dealt")
		healthCheck = 0
	elif playerAttack == "2" and opponentGen == 1:
		opponentHealth = opponentHealth - 10
		if opponentHealth <= 0:
			os.system('clear')
			print("Congratulations! " + opponent + " has been defeated! You won!")
			quit()
		elif playerHealth <= 0:
			os.system('clear')
			print("You have been defeated!")
			quit()
		os.system('clear')
		attackbanner()
		print("\n" + opponent + " defended against the attack. 10 DMG was dealt")
		healthCheck = 0
	elif playerAttack == "2" and opponentGen == 2:
		playerHealth = playerHealth - 15
		if opponentHealth <= 0:
			os.system('clear')
			print("Congratulations! " + opponent + " has been defeated! You won!")
			quit()
		elif playerHealth <= 0:
			os.system('clear')
			print("You have been defeated!")
			quit()
		os.system('clear')
		attackbanner()
		print("\n" + opponent + " dodged your attack and struck you! You lose 15 HP")
		healthCheck = 0
	else:
		quit()

	raw_input("")


#-----------------------------------------------------------------------------------------------
#DEFEND CODE -----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------



	os.system('clear')
	attackbanner()
	print("\n\nIt's " + opponent + "\'s turn. How will you defend?\n")
	if player == "Bolin":
		print("1 - Block (Standard Attack Block)")
		print("2 - Rock Wall + Attack (Projectile Block/Attack)")
	elif player == "Katara":
		print("1 - Block (Standard Attack Block)")
		print("2 - Ice Wall + Attack (Projectile Block/Attack)")
	elif player == "Zuko":
		print("1 - Block (Standard Attack Block)")
		print("2 - Melt + Attack (Projectile Block/Attack)")
	elif player == "Tenzin":
		print("1 - Block (Standard Attack Block)")
		print("2 - Breeze + Attack (Projectile Block/Attack)")
	playerDefend = raw_input("\nDefend (1 or 2): ")
	opponentGen = random.choice(opponentGenList)
	if playerDefend == "1" and opponentGen == 1:
		os.system('clear')
		attackbanner()
		print("\nYou blocked! No damage was dealt!")
		raw_input("")
		attackLoop = 0
	elif playerDefend == "2" and opponentGen == 1:
		playerHealth = playerHealth - 20
		if opponentHealth <= 0:
			os.system('clear')
			print("Congratulations! " + opponent + " has been defeated! You won!")
			quit()
		elif playerHealth <= 0:
			os.system('clear')
			print("You have been defeated!")
			quit()
		os.system('clear')
		attackbanner()
		print("\nYou failed to block attack. 20 DMG was dealt")
		raw_input("")
		attackLoop = 0
		healthCheck = 0
	elif playerDefend == "1" and opponentGen == 2:
		playerHealth = playerHealth - 10
		if opponentHealth <= 0:
			os.system('clear')
			print("Congratulations! " + opponent + " has been defeated! You won!")
			quit()
		elif playerHealth <= 0:
			os.system('clear')
			print("You have been defeated!")
			quit()
		os.system('clear')
		attackbanner()
		print("\nYou defended against the attack. 10 DMG was dealt")
		raw_input("")
		attackLoop = 0
		healthCheck = 0
	elif playerDefend == "2" and opponentGen == 2:
		opponentHealth = opponentHealth - 15
		if opponentHealth <= 0:
			os.system('clear')
			print("Congratulations! " + opponent + " has been defeated! You won!")
			quit()
		elif playerHealth <= 0:
			os.system('clear')
			print("You have been defeated!")
			quit()
		os.system('clear')
		attackbanner()
		print("\nYou dodged the attack and struck " + opponent + "! Opponent loses 15 HP")
		raw_input("")
		attackLoop = 0
		healthCheck = 0
	else:
		quit()




		while healthCheck == 0:
			if opponentHealth <= 0:
				os.system('clear')
				print("Congratulations! " + opponent + " has been defeated! You won!")
				quit()
			elif playerHealth <= 0:
				os.system('clear')
				print("You have been defeated!")
				quit()
			else:
				healthCheck = 1
