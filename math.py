#!/usr/bin/python
def calculator():
	print("Type A for addition, S for subtraction, M for multiplication, or D for division!")
	n_calc = raw_input("/ ")
	if n_calc == "A":
		n_one = input("Number one: ")
		n_two = input("Number two: ")
		print(n_one + n_two);
		print("\n")
		calculator();
	elif n_calc == "S":
		n_one = input("Number one: ")
		n_two = input("Number two: ")
		print(n_one - n_two);
		print("\n")
		calculator();
	elif n_calc == "M":
		n_one = input("Number one: ")
		n_two = input("Number two: ")
		print(n_one * n_two);
		print("\n")
		calculator()
	elif n_calc == "D":
		n_one = input("Number one: ")
		n_two = input("Number two: ")
		print(n_one / n_two);
		print("\n")
		calculator()
	else:
		quit();

calculator()
