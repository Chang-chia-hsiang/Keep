#!/usr/bin/python3
import sys, os

def main():
	filename = 'differences.txt'
	try:
		os.remove(filename)
	except:
		pass
	linesA = 0
	linesB = 0
	listA = []
	with open(sys.argv[1],"r") as fileA:
		listA = fileA.readlines()
		linesA = len(listA)

	uncommons = 0
	with open(sys.argv[2],"r") as fileB:
		for string in fileB:
			linesB += 1
			if string not in listA:
				uncommons += 1
				with open(filename,"a") as fileC:
					fileC.write(string)
	
	if uncommons == 0 and linesA == linesB:
		print("The files are the same!")
	elif uncommons == 0 and linesA > linesB:
		print("The fileB is contained in A.")
	else:
		print("There are {} difference(s) in fileB.".format(uncommons))

if __name__ == "__main__":
	main()
