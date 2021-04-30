import sys
from prettytable import PrettyTable

def controler():

	arg1 = sys.argv[1]
	arg2 = sys.argv[2]
	arg1, arg2 = int(arg1), int(arg2)


	if arg1 > arg2:
		m = arg1
		n = arg2
	elif arg2 > arg1:
		m = arg2
		n = arg1
	else:
		print("Equal")

	print("Such that: m = n * q + r")
	table,gcd = ext_euclid(m,n)
	print(table)
	print("gcd:",gcd)


def formatter(steps):
	
	table = PrettyTable()
	table.field_names = ["m","n","q","r","a","b"]

	for step in steps:
		table.add_row(step)

	return table
		

def ext_euclid(m,n):
	
	steps = []
	k = 0

	r = 1
	a = 1
	b = 0

	steps.append(["","","","",a,b])
	k += 1

	while r > 0:
		r = m % n
		q = m // n
		
		if k == 1:
			a = 0
			b = 1
		else:
			a = steps[k-2][4] - (steps[k-1][2]*steps[k-1][4])
			b = steps[k-2][5] - (steps[k-1][2]*steps[k-1][5])

		steps.append([m,n,q,r,a,b])
		
		m = n
		n = r

		k += 1

	return formatter(steps),steps[-1][1]

controler()


