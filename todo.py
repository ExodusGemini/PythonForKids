#!/usr/bin/python
import os
i = 0
class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

os.system('clear')
##############################
##############################
wt = "Put together portfolio" #Today
wtm = "Nothing special going on tomorrow" #Tomorrow
wtw = "Nothing special going on this weekend" #This Weekend
wnw = "Nothing special going on next weekend" #Next Weekend
wnm = "Nothing special going on in the next 2 weeks" #Special Dates During Next 2 Weeks
##############################
##############################
##############################
mn = "Nothing special going on this month" #This Month
mnm = "Nothing special going on next month" #Next Month
manm = bcolors.GREEN + '''
January: X
February: X
March: X
April: X
May: X
June: X
July: #
August: #
September: #
October #
November: #
December: #
''' #After Next Month
##############################
##############################
##############################
y2k16 = "Finish with Shortridge" #2016
y2k17 = "" #2017
y2k18 = "#" #2018
y2k19 = "College!!!" #2019
##############################
##############################
TDL = raw_input(bcolors.GREEN + "(W)eek/(M)onth/(Y)ear?\n" + bcolors.ENDC)
if TDL == "W":
	os.system('clear')
	print(bcolors.GREEN + "Week Schedule\n-------------\n")
	print("Today: " + bcolors.ENDC + wt + "\n")
	print(bcolors.GREEN + "Tomorrow: " + bcolors.ENDC + wtm + "\n")
	print(bcolors.GREEN + "This Weekend: " + bcolors.ENDC + wtw + "\n")
	print(bcolors.GREEN + "Next Week: " + bcolors.ENDC + wnw + "\n")
	print(bcolors.GREEN + "Special Dates: " + bcolors.ENDC + wnm + "\n\n")
elif TDL == "M":
    os.system('clear')
    print(bcolors.GREEN + "Month Schedule\n--------------\n")
    print("This Month: " + bcolors.ENDC + mn + "\n")
    print(bcolors.GREEN + "Next Month: " + bcolors.ENDC + mnm + "\n")
elif TDL == "M+":
    os.system('clear')
    print(bcolors.GREEN + "Month Schedule\n--------------")
    print(bcolors.ENDC + manm + "\n")
elif TDL == "Y":
    os.system('clear')
    print("Year Schedule\n-------------\n")
    print("2016: " + y2k16 + "\n")
    print("2017: " + y2k17 + "\n")
    print("2018: " + y2k18 + "\n")
    print("2019: " + y2k19 + "\n\n")
else:
	quit()

while i < 2:
    i-1

