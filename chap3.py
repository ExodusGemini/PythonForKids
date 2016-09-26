#!/usr/bin/python
import os
class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
os.system('clear')
print("In Chapter 3 we talk about Strings\n\nAn example would be the following:\n\n\t" + bcolors.GREEN + "| fred = \"Why do gorillas have big nostrils? Big fingers!!\"\n\t| print(fred)" + bcolors.ENDC + "\n\nThen your terminal would print the string you assigned to \"fred\"")
print("\n\nFor example, assign something to fred")
fred = raw_input("\n\nfred = ")

os.system('clear')
print("fred = " + str(fred))
print("\n\nSo to print that, the command would be:\n\n" + bcolors.GREEN + "print(fred)" + bcolors.ENDC + "\n\nAnd the result would be:" + bcolors.GREEN)
print("\n> " + str(fred) + "\n\n\n")
