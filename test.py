#!/usr/bin/python3

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file",
                    help="display a file")
parser.add_argument("-p", "--print", help="print the file",
                    action="store_true")
parser.add_argument("-c", "--check", help="check the thermo massage of the file",
                    action="store_true")
parser.add_argument("-d", "--detail", help="print the detail thermo massage of the file",
                    action="store_true")
args = parser.parse_args()
answer = args.file

target = ["TotEng","KinEng","Temp","PotEng","E_bond","E_angle","E_dihed","E_impro","E_vdwl","E_coul","E_long","E_pair","E_mol","Press","Volume"]
data = {}
for term in target:
	data[term] = []

if args.print:
	with open(answer,"r") as file:
		for string in file:
			print(string)
elif args.check:
	with open(answer,"r") as file:
		for string in file:
			pieces = string.split()
			for piece in pieces:
				if piece in target and data[piece] != 1:
					data[piece] = 1
					print(piece)
			if len(pieces) > 0 and pieces[0] == "thermo":
				timestep = string.split()	
				print("Timestep:" + timestep[1])
elif args.detail:
	with open(answer,"r") as file:
		for string in file:
			pieces = string.split()
			for n in range(len(pieces)):
				if pieces[n] in target:
					data[pieces[n]].append(pieces[n+2])
			
				
					
		print(data)
				
else:
    print(answer)
