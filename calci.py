import sys, os, time
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
v = "\033[1;35m"
fm = y+"["+r+"+"+y+"]"
os.system("clear")
def banner():
	print g+"               C\033[1;31m4\033[1;32mLCuL\033[1;31m4\033[1;32mT\033[1;31m3\033[1;32mR"
	print""
	print""
	print v+"             [01]\033[1;34m Addition"
	print v+"             [02]\033[1;34m Subtraction"
	print v+"             [03]\033[1;34m Multiplication"
	print v+"             [04]\033[1;34m Division"
	print v+"             [05]\033[1;34m Squar A Number"
	print v+"             [06]\033[1;34m Remainder Find"
	print v+"             [07]\033[1;34m Max_Number"
	print v+"\n                [0]\033[1;32mExit"
	print""

def input():
	opt = raw_input(fm+g+"Enter Option (Number) : ")
	
	if opt =="1" or opt =="01":
		add()
	elif opt =="2" or opt =="02":
		sub()
	elif opt =="3" or opt =="03":
		multiply()
	elif opt =="4" or opt =="04":
		divide()
	elif opt =="05" or opt =="5":
		square()
	elif opt =="6" or opt =="06":
		remainder()
	elif opt =="7" or opt =="07":
		maxno()
	elif opt =="0":
		exit()
	else:
		_
		
def add():
	s = raw_input(fm +"Enter Numbe[x] : ")
	q = raw_input(fm +"Enter Number[y] : ")
	e = int(s) + int(q)
	print r+"\nAnswer : "+g, (e)
	return

def sub():
	s = raw_input(fm +"Enter Numbe[x] : ")
	q = raw_input(fm +"Enter Number[y] : ")
	e = int(s) - int(q)
	print r+"\nAnswer : "+g, (e)
	return
	
def multiply():
	s = raw_input(fm +"Enter Numbe[x] : ")
	q = raw_input(fm +"Enter Number[y] : ")
	e = int(s) * int(q)
	print r+"\nAnswer : "+g, (e)
	return
	
def divide():
	s = raw_input(fm +"Enter Numbe[x] : ")
	q = raw_input(fm +"Enter Number[y] : ")
	e = int(s) / int(q)
	print r+"\nAnswer : "+g, (e)
	return

def square():
	s = raw_input(fm +"Enter Numbe[x] : ")
	e = int(s) * int(s)
	print r+"\nAnswer : "+g, (e)
	return

def remainder():
	s = raw_input(fm +"Enter Numbe[x] : ")
	q = raw_input(fm +"Enter Number[y] : ")
	e = int(s) % int(q)
	print r+"\nAnswer : "+g, (e)
	return
	
def maxno():
	s = raw_input(fm +"Enter Numbe[x] : ")
	q = raw_input(fm +"Enter Number[y] : ")
	if int(s) > int(q):
		print r+"\nAnswer : "+g, (s)
	else:
		print r+"\nAnswer : "+g, (q)
	return
def exit():
	os.system("clear")
	os.system("login")
def main():
	try:
		banner()
		input()
	except KeyboardInterrupt:
		os.system("clear")
		banner()
		input()
main()