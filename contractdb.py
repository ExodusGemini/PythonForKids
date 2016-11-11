#!/usr/bin/python
import os, time
import random
con1Header = "Hack a school website"
con2Header = "Invent a hacking backpack"
con3Header = "#"
con4Header = "#"
con5Header = "#"
con6Header = "#"
con7Header = "#"
con1Full = "A privilege escalation request on www.sjva.org\nwas requested by an anonymous source.\nDue: December 5th, 2016"
con2Full = "The HackPack is a commissioned collective of\nhacking devices disguised as an innocent backpack.\nDue by: March 1st, 2017"
con3Full = "$"
con4Full = "$"
con5Full = "$"
con6Full = "$"
con7Full = "$"
con1Time = "24 days"
con2Time = "110 days (3.5 months)"
con3Time = "! hours"
con4Time = "! hours"
con5Time = "! days"
con6Time = "! days"
con7Time = "! hours"
i = 0
def contract1():
	os.system('clear')
	print("Contract 1 Accepted!\nYou have " + con1Time + " to complete this contract")
def contract2():
	os.system('clear')
	print("Contract 2 Accepted!\nYou have " + con2Time + " to complete this contract")
def contract3():
	os.system('clear')
	print("Contract 3 Accepted!\nYou have " + con3Time + " to complete this contract")
def contract4():
	os.system('clear')
	print("Contract 4 Accepted!\nYou have " + con4Time + " to complete this contract")
def contract5():
	os.system('clear')
	print("Contract 5 Accepted!\nYou have " + con5Time + " to complete this contract")
def contract6():
	os.system('clear')
	print("Contract 6 Accepted!\nYou have " + con6Time + " to complete this contract")
def contract7():
	os.system('clear')
	print("Contract 7 Accepted!\nYou have " + con7Time + " to complete this contract")
def contractList():
	print("\t\tAvailable Contracts\n\n1. " + con1Header + "\n2. " + con2Header + "\n3. " + con3Header + "\n4. " + con4Header + "\n5. " + con5Header + "\n6. " + con6Header + "\n7. " + con7Header + "\n")
contractList()
def selection():
	selectContract = raw_input("alconite@cDB:~# ")
	if str(selectContract) == "1":
		os.system('clear')
		print("\tContract 1 Details\n\n" + con1Header + "\n\n" + con1Full + "\n")
	elif str(selectContract) == "2":
                os.system('clear')
		print("\tContract 2 Details\n\n" + con2Header + "\n\n" + con2Full + "\n")
	elif str(selectContract) == "3":
                os.system('clear')
                print("\tContract 3 Details\n\n" + con3Header + "\n\n" + con3Full + "\n")
	elif str(selectContract) == "4":
                os.system('clear')
                print("\tContract 4 Details\n\n" + con4Header + "\n\n" + con4Full + "\n")
	elif str(selectContract) == "5":
                os.system('clear')
                print("\tContract 5 Details\n\n" + con5Header + "\n\n" + con5Full + "\n")
	elif str(selectContract) == "6":
                os.system('clear')
                print("\tContract 6 Details\n\n" + con6Header + "\n\n" + con6Full + "\n")
	elif str(selectContract) == "7":
                os.system('clear')
                print("\tContract 7 Details\n\n" + con7Header + "\n\n" + con7Full + "\n")
	elif str.lower(selectContract) == "quit":
		print("Disconnecting")
		exit(0)
	elif str.lower(selectContract) == "cancel":
		os.system('clear')
		contractList()
	elif str.lower(selectContract) == "show":
		os.system('clear')
		contractList()
	elif str.lower(selectContract) == "help" or str.lower(selectContract) == "h":
		os.system('clear')
		print("\tContract Database Commands\n\n\'1\' selects contract 1\n\'2\' selects contract 2\n\'3\' selects contract 3\n\'4\' selects contract 4\n\'5\' selects contract 5\n\'6\' selects contract 6\n\'7\' selects contract 7\n'quit' disconnects from the contract database\n\'help\' displays a list of commands\n'cancel' declines a contract and goes back to list\n'show' displays list of all contracts\n'accept' accepts a selected contract\n")
	elif str.lower(selectContract) == "accept":
		print("Usage: accept [contract number]\nexample: accept 1")
	elif str.lower(selectContract) == "accept 1":
		contract1()
	elif str.lower(selectContract) == "accept 2":
		contract2()
	elif str.lower(selectContract) == "accept 3":
		contract3()
	elif str.lower(selectContract) == "accept 4":
		contract4()
	elif str.lower(selectContract) == "accept 5":
		contract5()
	elif str.lower(selectContract) == "accept 6":
		contract6()
	elif str.lower(selectContract) == "accept 7":
		contract7()
	elif selectContract == '':
		pass	
	else:
		print("\'" + selectContract + "\' is not a valid command")
while i == 0:
	selection()

